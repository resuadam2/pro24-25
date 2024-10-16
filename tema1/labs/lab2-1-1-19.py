# Laboratorio 2.1.1.19 : Dando formato a la salida

# Punto de partida

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# Minimizar los prints añadiendo \n
# Forma 1
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

# Forma 2
print("    *", "   * *", "  *   *", " *     *", "***   ***", "  *   *", "  *   *", "  *****", sep="\n")

# Flecha el doble de grande pero proporcional

flecha = "    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n"

print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("****         ****")
print("   *         *")
print("   *         *")
print("   *         *")
print("   *         *")
print("   *         *")
print("   ***********")

# Duplicar la flecha, colocando ambas lado a lado a.k.a. en paralelo

print("    *         *")
print("   * *       * *")
print("  *   *     *   *")
print(" *     *   *     *")
print("***   *** ***   ***")
print("  *   *     *   *")
print("  *   *     *   *")
print("  *****     *****")

# Error forzado

# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print(***   ***) # Error, falta las comillas, pero python encuentra el error en el espacio ya que espera algo más tras el asterisco# print("  *   *")
# print("  *   *")
# print("  *****")

# Segundo error forzado

# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print"***   ***" # Error de sintaxis, toda llamada a una función debe llevar paréntesis
# print("  *   *")
# print("  *   *")
# print("  *****")

# Tercer error forzado

# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# Print("***   ***") # Error, Print no está definido, y python es case sensitive y además reconoce cuándo no tiene una función o variable definidas
# print("  *   *")
# print("  *   *")
# print("  *****")

# Reemplazar comillas por apóstrofes

print("    *")
print('   * *')
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")