import json
import requests
import os


def get_animal_data(animal_name):
    """Fetches animal data from the API Ninjas Animals API."""
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': 'XL3dO8k9/+HKpwX1qvA4zg==CHisXjRa9dlCb83o'})
    
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return None


def serialize_animal(animal_obj):
    """ Converts a single animal dictionary into an HTML list item.
        Returns formatted html string containing the animal's name, 
        diet, location, and type. """
    output = '<li class="cards__item">\n'
    output += f'    <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '    <p class="card__text">\n'

    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        output += f'        <strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'

    if "locations" in animal_obj and animal_obj["locations"]:
        output += f'        <strong>Location:</strong> {", ".join(animal_obj["locations"])}<br/>\n'

    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        output += f'        <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'

    output += '    </p>\n'
    output += '</li>\n'
    return output


def main():
    """Main function that gets user input, fetches data from API, and generates HTML."""
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    animal_name = input("Enter a name of an animal: ")
    animals_data = get_animal_data(animal_name)

    # Use the correct path to the template file
    template_path = os.path.join(script_dir, "animals_template.html")
    with open(template_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    if animals_data:
        animals_info = '<ul class="cards">\n'
        for animal in animals_data:
            animals_info += serialize_animal(animal)
        animals_info += "</ul>\n"
    else:
        animals_info = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # Save the generated HTML in the same directory as the script
    output_path = os.path.join(script_dir, "animals.html")
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)
    
    print(f"Website was successfully generated to the file: {output_path}")


if __name__ == "__main__":
    main()