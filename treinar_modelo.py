import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report


# 1. Carregar o dataset
df = pd.read_csv("data/dataset_cardioia.csv")

print("Dataset carregado com sucesso!")
print(f"Quantidade de registros: {len(df)}")


# 2. Separar variáveis de entrada (X) e variável-alvo (y)
X = df.drop(columns=["pico_risco"])
y = df["pico_risco"]


# 3. Separar dados de treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"\nRegistros para treino: {len(X_train)}")
print(f"Registros para teste: {len(X_test)}")


# 4. Criar e treinar o modelo
modelo = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

modelo.fit(X_train, y_train)


# 5. Fazer previsões
y_pred = modelo.predict(X_test)


# 6. Avaliar o modelo
acuracia = accuracy_score(y_test, y_pred)
matriz = confusion_matrix(y_test, y_pred)

print("\n--- RESULTADOS DO MODELO ---")
print(f"Acurácia: {acuracia:.4f}")

print("\nMatriz de Confusão:")
print(matriz)

print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))


# 7. Criar as pastas para os resultados
os.makedirs("models", exist_ok=True)
os.makedirs("resultados", exist_ok=True)


# 8. Salvar o modelo treinado
joblib.dump(modelo, "models/modelo_risco.pkl")

print("\nModelo salvo em: models/modelo_risco.pkl")


# 9. Gerar e salvar a matriz de confusão
disp = ConfusionMatrixDisplay(
    confusion_matrix=matriz,
    display_labels=["Sem pico", "Com pico"]
)

disp.plot()

plt.title("Matriz de Confusão - CardioIA")
plt.savefig(
    "resultados/matriz_confusao.png",
    bbox_inches="tight"
)

plt.close()

print("Matriz de confusão salva em: resultados/matriz_confusao.png")