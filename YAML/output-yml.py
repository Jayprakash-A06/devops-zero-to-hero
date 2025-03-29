import yaml

data = {
    "app": {
        "name": "MyApp",
        "version": "1.0.0"
    },
    "settings": {
        "debug": True,
        "max_retries": 5
    }
}

# Writing to a YAML file
with open("output.yaml", "w") as file:
    yaml.dump(data, file)

print("YAML file written successfully!")
