!pip install pandas, matplotlib, streamlit


# BIBLIOTECAS
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# DATASETS
df = pd.read_excel('novos.xlsx')


# Extraindo o ano para facilitar a filtragem depois
df['Ano'] = df['data'].dt.year


# Definir as colunas de infraestrutura
infra_colunas = ['Atualmente você: ',
'Atualmente, quantos empregos/trabalhos remunerados você tem (se você estiver cursando o doutorado como bolsista, marque nenhum)',
'HOJE EM DIA, você:  ',
'Se você estuda, qual nível?',
'Caso afirmativo na questão anterior, qual área de mestrado ou qual graduação?',
'Se você trabalha HOJE EM DIA, qual é natureza do seu trabalho:',
'Onde exerce sua atividade profissional atual?',
'Regime de contratação ATUAL',
'Você prestou algum concurso público para o cargo efetivo de docente após a sua pós-graduação?',
'Caso tenha mudado de atividade profissional, você atribuiria essa nova atividade à realização do mestrado em Saúde Coletiva?',
'Quanto à sua atividade profissional ATUAL, está relacionada ao mestrado que concluiu?',
'A conclusão do mestrado ocasionou algum aumento salarial?',
'No seu trabalho atual, você desenvolve algum projeto de pesquisa?',
'Se você atua como docente, qual o tipo de inserção?',
'Qual o tipo de disciplina você ministra atualmente?',
'Se atua como docente, desenvolve algum projeto de pesquisa?',
'Você está inserido/participa de algum grupo de pesquisa?',
'Atualmente você participa de algum comitê, comissão ou assessoria em políticas públicas de saúde ou na área de ciência de tecnologia?',
'Caso você participe, especificar qual.',
'Infraestrutura dedicada à gestão do mestrado – secretaria, coordenação, etc. ',
'Estrutura curricular em termos do quanto permitiu aprendizagens significativas no mestrado',
'Infraestrutura para ensino usada no mestrado - salas de aula, biblioteca, serviços de videoconferência, laboratórios, etc. ',
'Suporte oferecido pelo(s) orientador(es) para o desenvolvimento do seu trabalho final',
'Perfil (formação e experiência) do corpo docente para a manutenção e a qualidade das atividades do mestrado',
'Dedicação do corpo docente para a manutenção e a qualidade das atividades do mestrado',
'Contribuiu para a melhora da sua renda ',
'Contribuiu para a sua empregabilidade',
'Contribuiu para o seu crescimento profissional',
'Contribuiu para definição de um campo de interesse temático para pesquisa e atuação profissional',
'Me capacitou para exercer a docência no ensino superior na minha área',
'Me capacitou para conceber e desenvolver projetos de pesquisas no meu campo de conhecimento',
'Ampliou a minha capacitação para atuar profissionalmente na minha área',
'Ampliou a minha capacitação para conceber e desenvolver projetos de extensão e serviços para segmentos da sociedade',
'Publicou algum item AO LONGO DO MESTRADO?'

]  # Adicione todas as colunas de infraestrutura aqui


# Título do aplicativo
st.title("Autoavaliação PPGSC - Pesquisa docente")

# Seleção de múltiplos anos
anos_selecionados = st.multiselect("Selecione os Anos:", df['Ano'].unique(), default=df['Ano'].unique()[:2])

# Seleção da coluna de infraestrutura
infra_selecionada = st.selectbox("Selecione a Coluna", infra_colunas, key="selectbox_infra")

# Filtrar os dados para os anos selecionados e a coluna de infraestrutura
df_filtrado = df[df['Ano'].isin(anos_selecionados)]

# Transformar o DataFrame em formato longo
df_melted = pd.melt(df_filtrado, id_vars=['Ano'], value_vars=[infra_selecionada], 
                    var_name='Infraestrutura', value_name='Categoria')

# Contar as ocorrências de cada categoria
contagem_df = df_melted.groupby(['Ano', 'Infraestrutura', 'Categoria']).size().reset_index(name='Contagem')

# Configurar o gráfico
plt.figure(figsize=(12, 8))

# Criar o gráfico de barras com hue
sns.set(style="whitegrid")
g = sns.barplot(
    data=contagem_df, x="Categoria", y="Contagem", hue="Ano", palette="Set1", ci=None
)

# Ajustar o título e os rótulos
g.set_title(f"Avaliação dos docentes para {infra_selecionada}", fontsize = 16)
g.set_xlabel("Avaliação")
g.set_ylabel("Frequência")

# Mostrar o gráfico no Streamlit
st.pyplot(plt)

plt.close()  # Fecha a figura para evitar duplicações

# streamlit run dash_ppgsc2.py
