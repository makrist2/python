import csv
from pprint import pprint as pp


def get_data_from_csv(filename):
    f = open(filename, "r")
    list_dicts = [row for row in csv.DictReader(f)]
    f.close()
    return list_dicts


def survived_percentage(passengers, field):
    if field == 'Sex':
        surv_sex_info = {'male_survived': 0,
                         'female_survived': 0,
                         'total_male': 0,
                         'total_female': 0}
        for fieldd in passengers:
            if fieldd['Sex'] == 'male':
                if fieldd['Survived'] == '1':
                    surv_sex_info['male_survived'] += 1
                surv_sex_info['total_male'] += 1
            if fieldd['Sex'] == 'female':
                if fieldd['Survived'] == '1':
                    surv_sex_info['female_survived'] += 1
                surv_sex_info['total_female'] += 1
        survived = {
            field: {'Male': '{:.2%}'.format(surv_sex_info['male_survived'] / surv_sex_info['total_male']),
                    'Female': '{:.2%}'.format(surv_sex_info['female_survived'] / surv_sex_info['total_female'])}
        }
        return survived

    elif field == 'Pclass':
        class_surv_info = {
            'first_class_survived': 0,
            'second_class_survived': 0,
            'third_class_survived': 0,
            'total_first_class': 0,
            'total_second_class': 0,
            'total_third_class': 0}

        for fieldd in passengers:
            if fieldd['Pclass'] == '1':
                if fieldd['Survived'] == '1':
                    class_surv_info['first_class_survived'] += 1
                class_surv_info['total_first_class'] += 1
            if fieldd['Pclass'] == '2':
                if fieldd['Survived'] == '1':
                    class_surv_info['second_class_survived'] += 1
                class_surv_info['total_second_class'] += 1
            if fieldd['Pclass'] == '3':
                if fieldd['Survived'] == '1':
                    class_surv_info['third_class_survived'] += 1
                class_surv_info['total_third_class'] += 1

        survived = {
            field: {'First class survived percentage': '{:.2%}'.format(
                class_surv_info['first_class_survived'] / class_surv_info['total_first_class']),
                    'Second class survived percentage': '{:.2%}'.format(
                        class_surv_info['second_class_survived'] / class_surv_info['total_second_class']),
                    'Third class survived percentage': '{:.2%}'.format(
                        class_surv_info['third_class_survived'] / class_surv_info['total_third_class'])}
        }
        return survived


pp(survived_percentage(get_data_from_csv('titanic.csv'), 'Sex'))
pp(survived_percentage(get_data_from_csv('titanic.csv'), 'Pclass'))

# pp(get_data_from_csv('titanic.csv'))
