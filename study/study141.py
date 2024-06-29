import re
import tkinter as tk
from tkinter import messagebox

def extract_ingredients(recipe):
   
    ingredient_pattern = re.compile(r'\b(?:양파|마늘|소금|후추|고기|채소|간장|설탕|고추장|된장|감자|당근|시금치)\b')
    ingredients = ingredient_pattern.findall(recipe)
    return set(ingredients)  

def show_ingredients():
    recipe = recipe_text.get("1.0", tk.END).strip()
    ingredients = extract_ingredients(recipe)

    if ingredients:
        result = "필요한 재료 목록:\n" + "\n".join(f"- {ingredient}" for ingredient in ingredients)
    else:
        result = "레시피에서 필요한 재료를 찾을 수 없습니다."

    messagebox.showinfo("결과", result)


root = tk.Tk()
root.title("레시피 재료 추출기")

tk.Label(root, text="레시피를 입력하세요:").pack(pady=10)
recipe_text = tk.Text(root, width=50, height=10)
recipe_text.pack(pady=10)

tk.Button(root, text="재료 추출", command=show_ingredients).pack(pady=10)

root.mainloop()
