
"""
Click detection: determines whether a click hits a balloon.
"""


def check_pop(balloons, click_pos):
    """
    Return the balloon clicked, or None if no balloon was hit.
    """
    for balloon in balloons:
        dx = click_pos[0] - balloon.x
        dy = click_pos[1] - balloon.y

        distance_squared = dx * dx + dy * dy

        # Compare squared distance with squared radius.
        if distance_squared <= balloon.radius * balloon.radius:
            return balloon

    return None
