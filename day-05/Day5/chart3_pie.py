# NCV Level 4 | Enrichment Charts | example: e_pie
# Type it in Thonny, run it, then change one thing.
import matplotlib.pyplot as plt

marks = [65, 72, 58, 48, 81, 39, 90, 55]

passed = 0
failed = 0
distinction = 0
for m in marks:
    if m >= 80:
        distinction = distinction + 1
    elif m >= 50:
        passed = passed + 1
    else:        
        failed = failed + 1
print(passed, failed, distinction)

plt.pie([passed, failed, distinction], labels=["Pass", "Fail", "Distinction"],
        colors=["#2E8B57", "#E31E3B", "#FFA500"], autopct="%1.0f%%")
plt.title("Pass,distinction & fail ")
plt.show()
