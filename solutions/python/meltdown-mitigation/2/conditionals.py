"""Functions to prevent a nuclear meltdown."""

CRITICAL_TEMPERATURE_LIMIT = 800
NEUTRONS_EMITTED_LIMIT = 500
TEMP_AND_NEUTRONS_PRODUCT = 500000

def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    if temperature < CRITICAL_TEMPERATURE_LIMIT and neutrons_emitted > NEUTRONS_EMITTED_LIMIT and (temperature * neutrons_emitted < TEMP_AND_NEUTRONS_PRODUCT):
        return True
    return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    
    generated_power = voltage * current
    efficiency = generated_power / theoretical_max_power
    efficiency_percent = efficiency * 100

    if efficiency_percent < 30:
        return 'black'
    if efficiency_percent >= 30 and efficiency_percent < 60:
        return 'red'
    if efficiency_percent >= 60 and efficiency_percent < 80:
        return 'orange'
    else:
        return 'green'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    temp_neutron_multiple = temperature * neutrons_produced_per_second

    minimal_threshold = threshold * 0.9
    maximum_threshold = threshold * 1.1

    if temp_neutron_multiple < (0.9 * threshold):
        return 'LOW'
    elif temp_neutron_multiple >= minimal_threshold and temp_neutron_multiple <= maximum_threshold:
        return 'NORMAL'
    else:
        return 'DANGER'
    
