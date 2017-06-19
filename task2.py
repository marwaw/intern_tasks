def damage(spell):
    """
    Function calculating damage
    :param str spell: string with spell
    :rtype: int
    :return: points of damage
    """

    spells_list = [('dai', 5), ('aine', 4), ('ain', 3), ('jee', 3), ('je', 2), ('ne', 2), ('ai', 2), ('fe', 1)]

    damage = 0

    if (is_correct(spell)):
        start_index = spell.find('fe')
        end_index = spell.rfind('ai') + 2

        new_spell = spell[start_index: end_index]

        for current_spell, current_val in spells_list:
            if(current_spell in new_spell):
                counter = new_spell.count(current_spell)
                damage += counter * current_val
                new_spell = new_spell.replace(current_spell, "")

        if (len(new_spell) > 0): damage -= len(new_spell)
        if (damage < 0): damage = 0

    return damage

def is_correct(spell):
    
    start_index = spell.find('fe')
    end_index = spell.rfind('ai')

    if (start_index < 0 or end_index < 0):
        return False

    is_more_fe = 'fe' in spell[start_index+2:]

    return start_index < end_index and not is_more_fe