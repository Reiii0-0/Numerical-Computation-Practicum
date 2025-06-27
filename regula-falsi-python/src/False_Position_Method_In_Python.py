import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def regula_falsi(f_expr, a, b, tol=1e-6, max_iter=100):
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr, 'numpy')

    if a == b:
        raise ValueError("Nilai a dan b tidak boleh sama.")
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) dan f(b) harus memiliki tanda yang berbeda (interval tidak valid).")

    print("\nIterasi Regula Falsi:")
    print("-" * 60)
    print(f"{'Iter':<5} {'a':<12} {'b':<12} {'c':<12} {'f(c)':<12}")
    print("-" * 60)
    
    for i in range(1, max_iter + 1):
        fa = f(a)
        fb = f(b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        
        print(f"{i:<5} {a:<12.6f} {b:<12.6f} {c:<12.6f} {fc:<12.6f}")
        
        if abs(fc) < tol:
            print("-" * 60)
            print(f"Konvergensi tercapai pada iterasi ke-{i}.")
            return c
        
        if fa * fc < 0:
            b = c
        else:
            a = c

    print("-" * 60)
    raise RuntimeError(f"Konvergensi tidak tercapai setelah {max_iter} iterasi.")

def plot_function(f_expr, root, a, b):
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr, 'numpy')

    x_vals = np.linspace(a - 1, b + 1, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(10, 6))
    plt.axhline(0, color='black', linewidth=0.5)
    plt.plot(x_vals, y_vals, label=f'f(x) = {str(f_expr)}')
    plt.plot(root, f(root), 'ro', label=f'Akar ≈ {root:.6f}')
    plt.plot(a, f(a), 'bo', label=f'Titik a = {a:.2f}')
    plt.plot(b, f(b), 'go', label=f'Titik b = {b:.2f}')
    
    plt.title("Metode Regula Falsi")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    
    if max(abs(y_vals)) > 1e6:
        plt.ylim(-10, 10)
    
    plt.show()

def main():
    print("Program Metode Regula Falsi")
    print("Contoh input persamaan: x**3 - 2*x - 5")
    
    try:
        user_input = input("Masukkan persamaan terhadap x: ")
        f_expr = sp.sympify(user_input)
        
        a = float(input("Masukkan nilai awal a: "))
        b = float(input("Masukkan nilai awal b: "))

        root = regula_falsi(f_expr, a, b)
        print(f"\nAkar yang ditemukan: {root:.8f}")
        plot_function(f_expr, root, a, b)
        
    except sp.SympifyError:
        print("Error: Persamaan tidak valid. Gunakan sintaks Python yang benar.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()