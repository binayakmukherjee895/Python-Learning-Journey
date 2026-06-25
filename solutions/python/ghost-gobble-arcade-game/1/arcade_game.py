"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active==True and touching_ghost==True:
        return True
    else:
        return False
    
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Can a ghost be eaten?

    """

    pass


def score(touching_power_pellet, touching_dot):
    if touching_dot==True or touching_power_pellet==True:
        return True
    else:
        return False
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    Parameters:
        touching_power_pellet (bool): Is the player touching a power pellet?
        touching_dot (bool): Is the player touching a dot?

    Returns:
        bool: Has the player scored or not?

    """

   


def lose(power_pellet_active, touching_ghost):
    if touching_ghost==True and power_pellet_active==False:
        return True
    else:
        return False
    


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots==True and not lose(power_pellet_active,touching_ghost):
        
        return True
        
    else:
        return False
    """Trigger the victory event when all dots have been eaten.

    Parameters:
        has_eaten_all_dots (bool): Has the player "eaten" all the dots?
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Has the player won the game?
    """

    pass
