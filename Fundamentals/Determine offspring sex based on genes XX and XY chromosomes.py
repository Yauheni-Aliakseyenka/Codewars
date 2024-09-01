'''
If the sperm contains the X chromosome, return "Congratulations! You're going to have a daughter.";
If the sperm contains the Y chromosome, return "Congratulations! You're going to have a son.";
'''


def chromosome_check(chromosome):
    if 'Y' in chromosome:
        return 'Congratulations! You\'re going to have a son.'
    else:
        return 'Congratulations! You\'re going to have a daughter.'


def chromosome_check1(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')