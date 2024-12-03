def minimum_orbs(potions, target, memo):
    
    if target in memo:
        return memo[target]
    
    
    if target not in potions:
        return 1
    
    
    min_orbs = float('inf')
    
    for ingredients in potions[target]:
        orbs_needed = 0
        for ingredient in ingredients:
            orbs_needed += minimum_orbs(potions, ingredient, memo)
        
        min_orbs = min(min_orbs, orbs_needed)
    
    memo[target] = min_orbs  
    return min_orbs


n = int(input())  
potions = {}  
for _ in range(n):
    recipe = input().strip()
    potion, ingredients = recipe.split("=")
    ingredients = ingredients.split("+")
    
    if potion not in potions:
        potions[potion] = []
    potions[potion].append(ingredients)


target_potion = input().strip()


memo = {}


result = minimum_orbs(potions, target_potion, memo)


print(result-1)