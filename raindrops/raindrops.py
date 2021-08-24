def convert(number: int) -> str:
    raindrops = ""
    
    factor_sounds = [
        (3, "Pling"),
        (5, "Plang"),
        (7, "Plong")
    ]
    
    sounds = "".join(
        sound
        for factor, sound in factor_sounds
        if number % factor == 0
    )
    
    return sounds or str(number)
