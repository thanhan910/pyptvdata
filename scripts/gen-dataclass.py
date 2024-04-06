import requests
import os

# FIELD_TYPES = set()

FIELD_TYPES_MAP = {
    'array': 'list', 
    'boolean': 'bool', 
    'integer': 'int', 
    'number': 'float', 
    'object': "object", 
    'string': 'str'
}

def get_dataclass_name(class_name):
    return 'V3' + class_name


def generate_dataclass(class_name, schema):
    fields = []
    class_dependencies = set()
    for prop_name, prop_schema in schema["properties"].items():
        if "type" in prop_schema:
            if prop_schema["type"] == "object":
                assert "additionalProperties" in prop_schema, f"Missing additionalProperties for {prop_name}"
                if "$ref" in prop_schema["additionalProperties"]:
                    field_type = prop_schema["additionalProperties"]["$ref"].split("#/definitions/V3.", 1)[1]
                    field_type = get_dataclass_name(field_type)
                    class_dependencies.add(field_type)
                else:
                    assert "type" in prop_schema["additionalProperties"], f"Missing type for {prop_name}"
                    field_type = prop_schema["additionalProperties"]["type"]
                    # FIELD_TYPES.add(field_type)
                    field_type = FIELD_TYPES_MAP[field_type]
                
            elif prop_schema["type"] == "array":
                if "type" in prop_schema["items"]:
                    inner_type = prop_schema["items"]["type"]
                    # FIELD_TYPES.add(inner_type)
                    inner_type = FIELD_TYPES_MAP[inner_type]
                    field_type = f"list[{inner_type}]"
                        
                else:
                    field_type = prop_schema["items"]["$ref"].split("#/definitions/V3.", 1)[1]
                    field_type = get_dataclass_name(field_type)
                    class_dependencies.add(field_type)
            else:
                field_type = prop_schema["type"]
                # FIELD_TYPES.add(field_type)
                field_type = FIELD_TYPES_MAP[field_type]
        else:
            field_type = prop_schema["$ref"].split("#/definitions/V3.", 1)[1]
            field_type = get_dataclass_name(field_type)
            class_dependencies.add(field_type)
        
        description = prop_schema.get("description", "")
        
        # fields.append(f"    {prop_name}: {field_type}\n    \"\"\"\n{description}\n\"\"\"")
        fields.append(f"    {prop_name}: {field_type}\n    \"\"\"\n    {description.replace("\n", "\n    ")}\n    \"\"\"")

    class_description = schema.get("description", "")

    class_field_signature = "\n".join(fields) if len(fields) > 0 else "    pass"

    return f"@dataclass\nclass {class_name}:\n    \"\"\"\n    {class_description.replace("\n", "\n    ")}\n    \"\"\"\n" + class_field_signature, class_dependencies


if __name__ == "__main__":

    docs_definitions : dict[str, dict] = requests.get('https://timetableapi.ptv.vic.gov.au/swagger/docs/v3').json()['definitions']

    # Generate dataclasses
    generated_codes = {}
    class_dependencies_map = {}
    # keys_set = set()
    for class_name, schema in docs_definitions.items():
        # for key in schema.keys():
        #     keys_set.add(key)
        dataclass_name = get_dataclass_name(class_name.split('.', 1)[1])
        generated_code, class_dependencies = generate_dataclass(dataclass_name, schema)
        generated_codes[dataclass_name] = generated_code
        class_dependencies_map[dataclass_name] = class_dependencies

    for class_name, dependencies in class_dependencies_map.items():
        for dependency in dependencies:
            assert dependency in class_dependencies_map, f"Missing {dependency}"

    class_ordered = []
    class_ordered_set = set()

    while len(class_dependencies_map) > len(class_ordered_set):
        for class_name, dependencies in class_dependencies_map.items():
            if class_name in class_ordered_set:
                continue
            if len(dependencies) == 0:
                class_ordered.append(class_name)
                class_ordered_set.add(class_name)
            else:
                class_dependencies_map[class_name] = dependencies - set(class_ordered)
    
    module_path = "../pyptvdata/apiv3/types.py"
    module_path = os.path.join(os.path.dirname(__file__), module_path)
    with open(module_path, 'w') as f:
        f.write("from dataclasses import dataclass\n\n\n")
        for class_name in class_ordered:
            f.write(generated_codes[class_name])
            f.write("\n\n")
