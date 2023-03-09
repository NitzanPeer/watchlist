from ..services import ui_service


def extract_title_and_year(options):

    extracted_data = []
    for option in options:
        extracted_data.append({
            'title': option['title'],
            'year': option['year'] if 'year' in option else option['release_date'][:4]
        })

    return extracted_data

def where_condition_handling(column, operator, value):

    return [
        {
            'column': column,
            'operator': operator,
            'value': value
        }
    ]