# В уявному двовимірному світі знаходиться гірський масив.
# Рельєф цього гірського масивузадано набором висот над рівнем моря{h1, h2…hn}.
# Після тривалих дощів долини між горами наповнились водою до найбільшого можливого рівня.
# Написати програму, яка знаходить глибину найглибшого озера.


def find_deepest_lake(heights: list):
    min_height = min(heights)
    differences = [height - min_height for height in heights]
    max_difference = max(differences)

    return max_difference


if __name__ == "__main__":
    heights = [0, 6, 1, 2, 3, 0, 1, 5, 6]
    depth = find_deepest_lake(heights)
    print(f"Глибина найглибшого озера: {depth}")