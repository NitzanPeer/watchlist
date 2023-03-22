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

def where_condition_looping(list_of_items, name_of_column, operator_type):
    result_clause = []

    if not isinstance(list_of_items, list):
        list_of_items = [list_of_items]

    for item in list_of_items:
        if operator_type == "like":
            operator = "LIKE"
            item = f"%{item}%"
        elif operator_type == "equals":
            operator = "="
        elif operator_type == "gte":
            operator = ">="


        result_clause.extend(where_condition_handling(name_of_column, operator, item))

    return [result_clause] if result_clause else []