import pandas as pd
import numpy as np
from scipy import stats

# --- CONFIGURAÇÕES ---
excel_path = "results/Effisegnet results.xlsx"  # Substitua pelo caminho do seu arquivo
sheet_name = "v3"                # Nome da aba onde estão os dados

# --- LEITURA DO EXCEL ---
df = pd.read_excel(excel_path, sheet_name=sheet_name)

# Remove espaços dos nomes das colunas (por segurança)
df.columns = [col.strip() for col in df.columns]

# Converte colunas de string com vírgula para float
metric_cols = [col for col in df.columns if col != "N fold"]
for col in metric_cols:
    df[col] = df[col].astype(str).str.replace(",", ".").astype(float)

# --- FUNÇÃO PARA CALCULAR MÉDIA E INTERVALO DE CONFIANÇA ---
def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)
    h = std_err * stats.t.ppf((1 + confidence) / 2., n-1)
    return mean, mean - h, mean + h

# --- CALCULANDO IC95 PARA CADA MÉTRICA ---
results = []
for col in metric_cols:
    mean, ci_lower, ci_upper = confidence_interval(df[col])
    results.append({
        "Métrica": col,
        "Média": round(mean, 6),
        "IC95% Inferior": round(ci_lower, 6),
        "IC95% Superior": round(ci_upper, 6)
    })

# --- RESULTADO FINAL ---
results_df = pd.DataFrame(results)
print(results_df)

# --- (Opcional) SALVAR EM NOVA ABA DO EXCEL ---
with pd.ExcelWriter(excel_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    results_df.to_excel(writer, sheet_name="IC_95", index=False)