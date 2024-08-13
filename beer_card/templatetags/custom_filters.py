from django import template

register = template.Library()

@register.filter
def star_rating(value):
    try:
        # Convert value to a float
        value = float(value)
    except (ValueError, TypeError):
        return ''  # Return empty string or an error message if conversion fails

    full_stars = int(value)  # Get the number of full stars
    half_star = 1 if value - full_stars >= 0.5 else 0  # Determine if there is a half star
    empty_stars = 5 - full_stars - half_star  # Calculate the number of empty stars
    
    stars = ('<i class="fa-solid fa-star"></i>' * full_stars) + \
            ('<i class="fa-solid fa-star-half"></i>' * half_star) + \
            ('<i class="fa-regular fa-star"></i>' * empty_stars)
    
    return stars

star_rating.is_safe = True  # Mark the output as safe HTML