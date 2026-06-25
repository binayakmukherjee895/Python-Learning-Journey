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
