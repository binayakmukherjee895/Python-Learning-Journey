def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature<800 and neutrons_emitted>500 and temperature*neutrons_emitted<500000:
        return True
    else:
        return False 

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power=voltage*current
    efficiency=(generated_power/theoretical_max_power)*100

    if efficiency>=80:
        return 'green'
    elif efficiency<80 and efficiency>=60:
        return 'orange'
    elif efficiency<60 and efficiency>=30:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    output_percentage=((temperature*neutrons_produced_per_second)/threshold)*100
    if output_percentage <90:
        return 'LOW'
    elif output_percentage>90 and output_percentage<110:
        return 'NORMAL'
    else:
        return 'DANGER'









    
    """Assess and return status code for the reactor.

    Parameters:
        temperature (int or float): The value of the temperature in kelvin.
        neutrons_produced_per_second (int or float): The neutron flux.
        threshold (int or float): The threshold for the category.

    Returns:
        str: One of ('LOW', 'NORMAL', 'DANGER').

    Note:
        1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
        2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
        3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    pass
