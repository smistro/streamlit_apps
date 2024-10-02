 # BIBLIOTECAS
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import time

# DATASETS
df = pd.read_csv('Pesquisa_docente_sem_dados.csv', sep = ';')

df['Data'] = pd.to_datetime(df['Data'])

# # Extraindo o ano para facilitar a filtragem depois
# df['Ano'] = df['Data'].dt.year


# RENOMEAR COLUNAS
df.rename(columns={
    'Infra_1_Infraestrutura das salas de aula': 'INFRAESTRUTURA (Salas de aula)',
    'Infra_2_Disponibilidade de recursos didáticos adequados': 'INFRAESTRUTURA (Recursos didáticos)',
    'Infra_3_Acervo da Biblioteca física e digital': 'INFRAESTRUTURA (Acervo da Biblioteca)',
    'Infra_4_Disponibilidade de acesso à Internet': 'INFRAESTRUTURA (Acesso à Internet)',
    'Infra_5_Adequação dos laboratórios às atividades de pesquisa': 'INFRAESTRUTURA (Laboratórios)',
    'Infra_6_Acessibilidade': 'INFRAESTRUTURA (Acessibilidade)',
    'Infra_7_Disponibilidade de sala multimídia com recursos para atividades via videoconferência': 'INFRAESTRUTURA (Sala multimídia / Videoconferência)',
    'Infra_8_Página do Programa com informações': 'INFRAESTRUTURA (Página do Programa)',
    'Gestão_1_Atuação da coordenação do programa': 'GESTÃO (Atuação da coordenação do programa)',
    'Gestão_2_Qualidade do atendimento prestado pela secretaria/funcionários' : 'GESTÃO (Qualidade do atendimento prestado pela secretaria/funcionários)',
    'Gestão_3_Comunicação e relacionamento da secretaria com os docentes' : 'GESTÃO (Comunicação e relacionamento da secretaria com os docentes)',
    'Gestão_4_Horário de atendimento da coordenação e secretaria do Programa' : 'GESTÃO (Horário de atendimento da coordenação e secretaria do Programa)',
    'Gestão_5_Comunicação e relacionamento dos discentes com a gestão colegiada interna do programa, com a direção do IMS' : 'GESTÃO (Comunicação e relacionamento dos discentes com a gestão colegiada interna do programa, com a direção do IMS)',
    'Gestão_6_Regularidade das reuniões do Colegiado do Programa' : 'GESTÃO (Regularidade das reuniões do Colegiado do Programa)',
    'Gestão_7_Utilização, aplicação equitativa e transparência na aplicação dos recursos do Programa de Apoio à Pós-graduação (PROAP)' : 'GESTÃO (Utilização, aplicação equitativa e transparência na aplicação dos recursos do Programa de Apoio à Pós-graduação (PROAP))',
    'Gestão_8_Articulação, aderência e atualização das áreas de concentração com as linhas de pesquisa do Programa' : 'GESTÃO (Articulação, aderência e atualização das áreas de concentração com as linhas de pesquisa do Programa)',
    'Gestão_9_Atualização e organização das disciplinas do programa' : 'GESTÃO (Atualização e organização das disciplinas do programa)',
    'Gestão_10_Interdisciplinaridade entre as disciplinas do programa' : 'GESTÃO (Interdisciplinaridade entre as disciplinas do programa)',
    'Gestão_11_Adequação das ementas das disciplinas à natureza do programa' : 'GESTÃO (Adequação das ementas das disciplinas à natureza do programa)',
    'Gestão_12_Adequação da carga horária das disciplinas' : 'GESTÃO (Adequação da carga horária das disciplinas)',
    'Gestão_13_Distribuição da carga horária total do programa' : 'GESTÃO (Distribuição da carga horária total do programa)',
    'Gestão_14_Cumprimento dos objetivos e missão do Programa' : 'GESTÃO (Cumprimento dos objetivos e missão do Programa)',
    'Gestão_15_Organização do processo de orientação de Dissertações' : 'GESTÃO (Organização do processo de orientação de Dissertações)',
    'Gestão_16_Atendimento do programa às expectativas do docente' : 'GESTÃO (Atendimento do programa às expectativas do docente)',
    'Gestão_17_Articulação de ensino de graduação e pós-graduação' : 'GESTÃO (Articulação de ensino de graduação e pós-graduação)',
    'Aval_disc_1_Processo de seleção discente' : 'AVALIAÇÃO DOS DISCENTES (Processo de seleção discente)',
    'Aval_disc_2_Quantidade de discentes no Programa' : 'AVALIAÇÃO DOS DISCENTES (Quantidade de discentes no Programa)',
    'Aval_disc_3_Assiduidade dos discentes às aulas' : 'AVALIAÇÃO DOS DISCENTES (Assiduidade dos discentes às aulas)',
    'Aval_disc_4_Pontualidade dos discentes às aulas' : 'AVALIAÇÃO DOS DISCENTES (Pontualidade dos discentes às aulas)',
    'Aval_disc_5_Participação dos discentes nas atividades da Pós-Graduação' : 'AVALIAÇÃO DOS DISCENTES (Participação dos discentes nas atividades da Pós-Graduação)',
    'Aval_disc_6_Relacionamento dos discentes com os docentes' : 'AVALIAÇÃO DOS DISCENTES (Relacionamento dos discentes com os docentes)',
    'Aval_disc_7_Dedicação dos discentes às leituras sugeridas pelos docentes' : 'AVALIAÇÃO DOS DISCENTES (Dedicação dos discentes às leituras sugeridas pelos docentes)',
    'Aval_disc_8_Motivação dos discentes para fazer o curso de mestrado' : 'AVALIAÇÃO DOS DISCENTES (Motivação dos discentes para fazer o curso de mestrado)',
    'Aval_disc_9_Qualidade dos trabalhos e avaliações apresentados pelos discentes' : 'AVALIAÇÃO DOS DISCENTES (Qualidade dos trabalhos e avaliações apresentados pelos discentes)',
    'Elab_dissert_1_Tempo que os seus orientandos disponibilizaram para elaboração da dissertação' : 'DISSERTAÇÃO (Tempo que os seus orientandos disponibilizaram para elaboração da dissertação)',
    'Elab_dissert_2_Relacionamento orientanda(o)/orientadora (o)' : 'DISSERTAÇÃO (Relacionamento orientanda(o)/orientadora (o))',
    'Elab_dissert_3_Qualidade das dissertações dos discentes do Programa' : 'DISSERTAÇÃO (Qualidade das dissertações dos discentes do Programa)',
    'Elab_dissert_4_Motivação dos discentes à publicação das dissertações' : 'DISSERTAÇÃO (Motivação dos discentes à publicação das dissertações)',
    'Pesquisa_1_Aderência do tema de pesquisa do discente à temática do grupo de pesquisa' : 'PESQUISA (Aderência do tema de pesquisa do discente à temática do grupo de pesquisa)',
    'Pesquisa_2_Articulação, aderência e atualização dos grupos de pesquisa com as linhas de pesquisa do Programa' : 'PESQUISA (Articulação, aderência e atualização dos grupos de pesquisa com as linhas de pesquisa do Programa)',
    'Pesquisa_3_Pontualidade dos discentes às reuniões do grupo de pesquisa' : 'PESQUISA (Pontualidade dos discentes às reuniões do grupo de pesquisa)',
    'Pesquisa_4_Assiduidade dos discentes às reuniões do grupo de pesquisa' : 'PESQUISA (Assiduidade dos discentes às reuniões do grupo de pesquisa)',
    'Pesquisa_5_Visibilidade dos grupos de pesquisa do programa' : 'PESQUISA (Visibilidade dos grupos de pesquisa do programa)',
    'Pesquisa_6_Regularidade de reuniões do grupo de pesquisa do qual faz parte' : 'PESQUISA (Regularidade de reuniões do grupo de pesquisa do qual faz parte)',
    'Pesquisa_7_Relação de interdisciplinaridade dos grupos de pesquisa do programa' : 'PESQUISA (Relação de interdisciplinaridade dos grupos de pesquisa do programa)',
    'Pesquisa_8_Padrão de internacionalização dos grupos de pesquisa' : 'PESQUISA (Padrão de internacionalização dos grupos de pesquisa)',
    'Pesquisa_9_Relação dos grupos de pesquisas com as atividades de extensão' : 'PESQUISA (Relação dos grupos de pesquisas com as atividades de extensão)',
    'Pesquisa_10_Ações de inovação tecnológica e geração de patentes no programa' : 'PESQUISA (Ações de inovação tecnológica e geração de patentes no programa)',
    'Pesquisa_11_Dedicação dos docentes a formação de parcerias e captação de recursos para a pesquisa' : 'PESQUISA (Dedicação dos docentes a formação de parcerias e captação de recursos para a pesquisa)',
    'Internac_1_Parcerias internacionais estabelecidas pelo programa' : 'INTERNACIONALIZAÇÃO (Parcerias internacionais estabelecidas pelo programa)',
    'Internac_2_Dedicação dos docentes à internacionalização' : 'INTERNACIONALIZAÇÃO (Dedicação dos docentes à internacionalização)',
    'Internac_3_Publicação docente-discente de artigos em periódicos com fator de impacto e/ou indexados em bases de dados (Scopus, Web of science, etc)' : 'INTERNACIONALIZAÇÃO (Publicação docente-discente de artigos em periódicos com fator de impacto e/ou indexados em bases de dados (Scopus, Web of science, etc))',
    'Internac_4_Publicação docente-discente de artigos em periódicos com qualis A' : 'INTERNACIONALIZAÇÃO (Publicação docente-discente de artigos em periódicos com qualis A)',
    'Internac_5_Publicação docente-discente de artigos em coautoria internacional' : 'INTERNACIONALIZAÇÃO (Publicação docente-discente de artigos em coautoria internacional)',
    'Internac_6_Publicação docente-discente de livros e/ou capítulos de livros' : 'INTERNACIONALIZAÇÃO (Publicação docente-discente de livros e/ou capítulos de livros)',
    'Internac_7_Presença de ações de fomento com impacto social no programa' : 'INTERNACIONALIZAÇÃO (Presença de ações de fomento com impacto social no programa)',
    'Internac_8_Ações de integração e cooperação com outros programas e centros de pesquisa e desenvolvimento profissional' : 'INTERNACIONALIZAÇÃO (Ações de integração e cooperação com outros programas e centros de pesquisa e desenvolvimento profissional)',
    'Internac_9_Produtos ou patentes com inserção no mercado' : 'INTERNACIONALIZAÇÃO (Produtos ou patentes com inserção no mercado)',
    'Autoav_docente_1_Motivação para fazer parte do Programa' : 'AUTOAVALIAÇÃO DOCENTE (Motivação para fazer parte do Programa)',
    'Autoav_docente_2_Qualidade, interdisciplinaridade e atualidade das pesquisas realizadas por você' : 'AUTOAVALIAÇÃO DOCENTE (Qualidade, interdisciplinaridade e atualidade das pesquisas realizadas por você)',
    'Autoav_docente_3_Inserção de suas pesquisas em grupo de pesquisa cadastrado' : 'AUTOAVALIAÇÃO DOCENTE (Inserção de suas pesquisas em grupo de pesquisa cadastrado)',
    'Autoav_docente_4_Aderência de suas orientações ao (s) grupo (s) de pesquisa do (s) qual (is) participa' : 'AUTOAVALIAÇÃO DOCENTE (Aderência de suas orientações ao (s) grupo (s) de pesquisa do (s) qual (is) participa)',
    'Autoav_docente_5_Aderência de seu (s) grupo (s) de pesquisa à linha de pesquisa da  qual faz parte' : 'AUTOAVALIAÇÃO DOCENTE (Aderência de seu (s) grupo (s) de pesquisa à linha de pesquisa da  qual faz parte)',
    'Autoav_docente_6_Regularidade e produtividade das reuniões do grupo de pesquisa' : 'AUTOAVALIAÇÃO DOCENTE (Regularidade e produtividade das reuniões do grupo de pesquisa)',
    'Autoav_docente_7_Produtividade e publicações conjuntas dos integrantes de seu grupo de pesquisa' : 'AUTOAVALIAÇÃO DOCENTE (Produtividade e publicações conjuntas dos integrantes de seu grupo de pesquisa)',
    'Autoav_docente_8_Interlocução externa (nacional e internacional) de seu grupo de pesquisa' : 'AUTOAVALIAÇÃO DOCENTE (Interlocução externa (nacional e internacional) de seu grupo de pesquisa)',
    'Autoav_docente_9_Qualidade dos planos de curso apresentados por você' : 'AUTOAVALIAÇÃO DOCENTE (Qualidade dos planos de curso apresentados por você)',
    'Autoav_docente_10_Planejamento e organização didática das suas atividades' : 'AUTOAVALIAÇÃO DOCENTE (Planejamento e organização didática das suas atividades)',
    'Autoav_docente_11_Formas e critérios de avaliação utilizados por você' : 'AUTOAVALIAÇÃO DOCENTE (Formas e critérios de avaliação utilizados por você)',
    'Autoav_docente_12_Adequação e atualidade da bibliografia utilizada por você' : 'AUTOAVALIAÇÃO DOCENTE (Adequação e atualidade da bibliografia utilizada por você)',
    'Autoav_docente_13_Relacionamento com a turma' : 'AUTOAVALIAÇÃO DOCENTE (Relacionamento com a turma)',
    'Autoav_docente_14_Clareza na exposição/orientação dos conteúdos' : 'AUTOAVALIAÇÃO DOCENTE (Clareza na exposição/orientação dos conteúdos)',
    'Autoav_docente_15_Assiduidade/pontualidade às atividades didáticas e de pesquisa' : 'AUTOAVALIAÇÃO DOCENTE (Assiduidade/pontualidade às atividades didáticas e de pesquisa)',
    'Autoav_docente_16_Disponibilidade em ministrar componentes curriculares no mestrado' : 'AUTOAVALIAÇÃO DOCENTE (Disponibilidade em ministrar componentes curriculares no mestrado)',
    'Autoav_docente_17_Dedicação aos componentes ministrados' : 'AUTOAVALIAÇÃO DOCENTE (Dedicação aos componentes ministrados)',
    'Autoav_docente_18_Orientação na elaboração da Dissertação/Produto' : 'AUTOAVALIAÇÃO DOCENTE (Orientação na elaboração da Dissertação/Produto)',
    'Autoav_docente_19_Tempo que disponibiliza para seus orientandos' : 'AUTOAVALIAÇÃO DOCENTE (Tempo que disponibiliza para seus orientandos)',
    'Autoav_docente_20_Interlocução entre aulas e pesquisas' : 'AUTOAVALIAÇÃO DOCENTE (Interlocução entre aulas e pesquisas)',
    'Autoav_docente_21_Disponilidade em compor comissões do mestrado' : 'AUTOAVALIAÇÃO DOCENTE (Disponilidade em compor comissões do mestrado)',
    'Autoav_docente_22_Disponibilidade em colaborar em atividades diversas do mestrado que são solicitadas' : 'AUTOAVALIAÇÃO DOCENTE (Disponibilidade em colaborar em atividades diversas do mestrado que são solicitadas)'
}, inplace=True)

# Definir as colunas de infraestrutura
colunas = [
    'INFRAESTRUTURA (Salas de aula)', 
    'INFRAESTRUTURA (Recursos didáticos)',
    'INFRAESTRUTURA (Acervo da Biblioteca)',
    'INFRAESTRUTURA (Acesso à Internet)',
    'INFRAESTRUTURA (Laboratórios)',
    'INFRAESTRUTURA (Acessibilidade)',
    'INFRAESTRUTURA (Sala multimídia / Videoconferência)',
    'INFRAESTRUTURA (Página do Programa)',
    'GESTÃO (Atuação da coordenação do programa)',
    'GESTÃO (Qualidade do atendimento prestado pela secretaria/funcionários)',
    'GESTÃO (Comunicação e relacionamento da secretaria com os docentes)',
    'GESTÃO (Horário de atendimento da coordenação e secretaria do Programa)',
    'GESTÃO (Comunicação e relacionamento dos discentes com a gestão colegiada interna do programa, com a direção do IMS)',
    'GESTÃO (Regularidade das reuniões do Colegiado do Programa)',
    'GESTÃO (Utilização, aplicação equitativa e transparência na aplicação dos recursos do Programa de Apoio à Pós-graduação (PROAP))',
    'GESTÃO (Articulação, aderência e atualização das áreas de concentração com as linhas de pesquisa do Programa)',
    'GESTÃO (Atualização e organização das disciplinas do programa)',
    'GESTÃO (Interdisciplinaridade entre as disciplinas do programa)',
    'GESTÃO (Adequação das ementas das disciplinas à natureza do programa)',
    'GESTÃO (Adequação da carga horária das disciplinas)',
    'GESTÃO (Distribuição da carga horária total do programa)',
    'GESTÃO (Cumprimento dos objetivos e missão do Programa)',
    'GESTÃO (Organização do processo de orientação de Dissertações)',
    'GESTÃO (Atendimento do programa às expectativas do docente)',
    'GESTÃO (Articulação de ensino de graduação e pós-graduação)',
    'AVALIAÇÃO DOS DISCENTES (Processo de seleção discente)',
    'AVALIAÇÃO DOS DISCENTES (Quantidade de discentes no Programa)',
    'AVALIAÇÃO DOS DISCENTES (Assiduidade dos discentes às aulas)',
    'AVALIAÇÃO DOS DISCENTES (Pontualidade dos discentes às aulas)',
    'AVALIAÇÃO DOS DISCENTES (Participação dos discentes nas atividades da Pós-Graduação)',
    'AVALIAÇÃO DOS DISCENTES (Relacionamento dos discentes com os docentes)',
    'AVALIAÇÃO DOS DISCENTES (Dedicação dos discentes às leituras sugeridas pelos docentes)',
    'AVALIAÇÃO DOS DISCENTES (Motivação dos discentes para fazer o curso de mestrado)',
    'AVALIAÇÃO DOS DISCENTES (Qualidade dos trabalhos e avaliações apresentados pelos discentes)',
    'DISSERTAÇÃO (Tempo que os seus orientandos disponibilizaram para elaboração da dissertação)',
    'DISSERTAÇÃO (Relacionamento orientanda(o)/orientadora (o))',
    'DISSERTAÇÃO (Qualidade das dissertações dos discentes do Programa)',
    'DISSERTAÇÃO (Motivação dos discentes à publicação das dissertações)',
    'PESQUISA (Aderência do tema de pesquisa do discente à temática do grupo de pesquisa)',
    'PESQUISA (Articulação, aderência e atualização dos grupos de pesquisa com as linhas de pesquisa do Programa)',
    'PESQUISA (Pontualidade dos discentes às reuniões do grupo de pesquisa)',
    'PESQUISA (Assiduidade dos discentes às reuniões do grupo de pesquisa)',
    'PESQUISA (Visibilidade dos grupos de pesquisa do programa)',
    'PESQUISA (Regularidade de reuniões do grupo de pesquisa do qual faz parte)',
    'PESQUISA (Relação de interdisciplinaridade dos grupos de pesquisa do programa)',
    'PESQUISA (Padrão de internacionalização dos grupos de pesquisa)',
    'PESQUISA (Relação dos grupos de pesquisas com as atividades de extensão)',
    'PESQUISA (Ações de inovação tecnológica e geração de patentes no programa)',
    'PESQUISA (Dedicação dos docentes a formação de parcerias e captação de recursos para a pesquisa)',
    'INTERNACIONALIZAÇÃO (Parcerias internacionais estabelecidas pelo programa)',
    'INTERNACIONALIZAÇÃO (Dedicação dos docentes à internacionalização)',
    'INTERNACIONALIZAÇÃO (Publicação docente-discente de artigos em periódicos com fator de impacto e/ou indexados em bases de dados (Scopus, Web of science, etc))',
    'INTERNACIONALIZAÇÃO (Publicação docente-discente de artigos em periódicos com qualis A)',
    'INTERNACIONALIZAÇÃO (Publicação docente-discente de artigos em coautoria internacional)',
    'INTERNACIONALIZAÇÃO (Publicação docente-discente de livros e/ou capítulos de livros)',
    'INTERNACIONALIZAÇÃO (Presença de ações de fomento com impacto social no programa)',
    'INTERNACIONALIZAÇÃO (Ações de integração e cooperação com outros programas e centros de pesquisa e desenvolvimento profissional)',
    'INTERNACIONALIZAÇÃO (Produtos ou patentes com inserção no mercado)',
    'AUTOAVALIAÇÃO DOCENTE (Motivação para fazer parte do Programa)',
    'AUTOAVALIAÇÃO DOCENTE (Qualidade, interdisciplinaridade e atualidade das pesquisas realizadas por você)',
    'AUTOAVALIAÇÃO DOCENTE (Inserção de suas pesquisas em grupo de pesquisa cadastrado)',
    'AUTOAVALIAÇÃO DOCENTE (Aderência de suas orientações ao (s) grupo (s) de pesquisa do (s) qual (is) participa)',
    'AUTOAVALIAÇÃO DOCENTE (Aderência de seu (s) grupo (s) de pesquisa à linha de pesquisa da  qual faz parte)',
    'AUTOAVALIAÇÃO DOCENTE (Regularidade e produtividade das reuniões do grupo de pesquisa)',
    'AUTOAVALIAÇÃO DOCENTE (Produtividade e publicações conjuntas dos integrantes de seu grupo de pesquisa)',
    'AUTOAVALIAÇÃO DOCENTE (Interlocução externa (nacional e internacional) de seu grupo de pesquisa)',
    'AUTOAVALIAÇÃO DOCENTE (Qualidade dos planos de curso apresentados por você)',
    'AUTOAVALIAÇÃO DOCENTE (Planejamento e organização didática das suas atividades)',
    'AUTOAVALIAÇÃO DOCENTE (Formas e critérios de avaliação utilizados por você)',
    'AUTOAVALIAÇÃO DOCENTE (Adequação e atualidade da bibliografia utilizada por você)',
    'AUTOAVALIAÇÃO DOCENTE (Relacionamento com a turma)',
    'AUTOAVALIAÇÃO DOCENTE (Clareza na exposição/orientação dos conteúdos)',
    'AUTOAVALIAÇÃO DOCENTE (Assiduidade/pontualidade às atividades didáticas e de pesquisa)',
    'AUTOAVALIAÇÃO DOCENTE (Disponibilidade em ministrar componentes curriculares no mestrado)',
    'AUTOAVALIAÇÃO DOCENTE (Dedicação aos componentes ministrados)',
    'AUTOAVALIAÇÃO DOCENTE (Orientação na elaboração da Dissertação/Produto)',
    'AUTOAVALIAÇÃO DOCENTE (Tempo que disponibiliza para seus orientandos)',
    'AUTOAVALIAÇÃO DOCENTE (Interlocução entre aulas e pesquisas)',
    'AUTOAVALIAÇÃO DOCENTE (Disponilidade em compor comissões do mestrado)',
    'AUTOAVALIAÇÃO DOCENTE (Disponibilidade em colaborar em atividades diversas do mestrado que são solicitadas)',
]  # Adicione todas as colunas de infraestrutura aqui

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Definir as colunas de infraestrutura e agrupar por categoria
grupos = {
    'INFRAESTRUTURA': [
        'INFRAESTRUTURA (Salas de aula)', 
        'INFRAESTRUTURA (Recursos didáticos)',
        'INFRAESTRUTURA (Acervo da Biblioteca)',
        'INFRAESTRUTURA (Acesso à Internet)',
        'INFRAESTRUTURA (Laboratórios)',
        'INFRAESTRUTURA (Acessibilidade)',
        'INFRAESTRUTURA (Sala multimídia / Videoconferência)',
        'INFRAESTRUTURA (Página do Programa)',
    ],
    'GESTÃO': [
        'GESTÃO (Atuação da coordenação do programa)',
        'GESTÃO (Qualidade do atendimento prestado pela secretaria/funcionários)',
        'GESTÃO (Comunicação e relacionamento da secretaria com os docentes)',
        # Adicione outras colunas relacionadas à GESTÃO aqui
    ],
    'AVALIAÇÃO DOS DISCENTES': [
        'AVALIAÇÃO DOS DISCENTES (Processo de seleção discente)',
        'AVALIAÇÃO DOS DISCENTES (Quantidade de discentes no Programa)',
        'AVALIAÇÃO DOS DISCENTES (Assiduidade dos discentes às aulas)',
        'AVALIAÇÃO DOS DISCENTES (Pontualidade dos discentes às aulas)',
        'AVALIAÇÃO DOS DISCENTES (Participação dos discentes nas atividades da Pós-Graduação)',
        'AVALIAÇÃO DOS DISCENTES (Relacionamento dos discentes com os docentes)',
        'AVALIAÇÃO DOS DISCENTES (Dedicação dos discentes às leituras sugeridas pelos docentes)',
        'AVALIAÇÃO DOS DISCENTES (Motivação dos discentes para fazer o curso de mestrado)',
        'AVALIAÇÃO DOS DISCENTES (Qualidade dos trabalhos e avaliações apresentados pelos discentes)'
        # Adicione outras colunas relacionadas à AVALIAÇÃO DOS DISCENTES aqui
    ],
    'DISSERTAÇÃO': [
        'DISSERTAÇÃO (Tempo que os seus orientandos disponibilizaram para elaboração da dissertação)',
        'DISSERTAÇÃO (Relacionamento orientanda(o)/orientadora (o))',
        'DISSERTAÇÃO (Qualidade das dissertações dos discentes do Programa)',
        'DISSERTAÇÃO (Motivação dos discentes à publicação das dissertações)'
    ],
    'PESQUISA': [
        'PESQUISA (Aderência do tema de pesquisa do discente à temática do grupo de pesquisa)',
        'PESQUISA (Articulação, aderência e atualização dos grupos de pesquisa com as linhas de pesquisa do Programa)',
        'PESQUISA (Pontualidade dos discentes às reuniões do grupo de pesquisa)',
        'PESQUISA (Assiduidade dos discentes às reuniões do grupo de pesquisa)',
        'PESQUISA (Visibilidade dos grupos de pesquisa do programa)',
        'PESQUISA (Regularidade de reuniões do grupo de pesquisa do qual faz parte)',
        'PESQUISA (Relação de interdisciplinaridade dos grupos de pesquisa do programa)',
        'PESQUISA (Padrão de internacionalização dos grupos de pesquisa)',
        'PESQUISA (Relação dos grupos de pesquisas com as atividades de extensão)',
        'PESQUISA (Ações de inovação tecnológica e geração de patentes no programa)',
        'PESQUISA (Dedicação dos docentes a formação de parcerias e captação de recursos para a pesquisa)'
    
     ],
    'INTERNACIONALIZAÇÃO': [
        'INTERNACIONALIZAÇÃO (Parcerias internacionais estabelecidas pelo programa)',
        'INTERNACIONALIZAÇÃO (Dedicação dos docentes à internacionalização)',
        'INTERNACIONALIZAÇÃO (Publicação docente-discente de artigos em periódicos com fator de impacto e/ou indexados em bases de dados (Scopus, Web of science, etc))',
        'INTERNACIONALIZAÇÃO (Publicação docente-discente de artigos em periódicos com qualis A)',
        'INTERNACIONALIZAÇÃO (Publicação docente-discente de artigos em coautoria internacional)',
        'INTERNACIONALIZAÇÃO (Publicação docente-discente de livros e/ou capítulos de livros)',
        'INTERNACIONALIZAÇÃO (Presença de ações de fomento com impacto social no programa)',
        'INTERNACIONALIZAÇÃO (Ações de integração e cooperação com outros programas e centros de pesquisa e desenvolvimento profissional)',
        'INTERNACIONALIZAÇÃO (Produtos ou patentes com inserção no mercado)'
    ],
    'AUTOAVALIAÇÃO DOCENTE': [
        'AUTOAVALIAÇÃO DOCENTE (Motivação para fazer parte do Programa)',
        'AUTOAVALIAÇÃO DOCENTE (Qualidade, interdisciplinaridade e atualidade das pesquisas realizadas por você)',
        'AUTOAVALIAÇÃO DOCENTE (Inserção de suas pesquisas em grupo de pesquisa cadastrado)',
        'AUTOAVALIAÇÃO DOCENTE (Aderência de suas orientações ao (s) grupo (s) de pesquisa do (s) qual (is) participa)',
        'AUTOAVALIAÇÃO DOCENTE (Aderência de seu (s) grupo (s) de pesquisa à linha de pesquisa da  qual faz parte)',
        'AUTOAVALIAÇÃO DOCENTE (Regularidade e produtividade das reuniões do grupo de pesquisa)',
        'AUTOAVALIAÇÃO DOCENTE (Produtividade e publicações conjuntas dos integrantes de seu grupo de pesquisa)',
        'AUTOAVALIAÇÃO DOCENTE (Interlocução externa (nacional e internacional) de seu grupo de pesquisa)',
        'AUTOAVALIAÇÃO DOCENTE (Qualidade dos planos de curso apresentados por você)',
        'AUTOAVALIAÇÃO DOCENTE (Planejamento e organização didática das suas atividades)',
        'AUTOAVALIAÇÃO DOCENTE (Formas e critérios de avaliação utilizados por você)',
        'AUTOAVALIAÇÃO DOCENTE (Adequação e atualidade da bibliografia utilizada por você)',
        'AUTOAVALIAÇÃO DOCENTE (Relacionamento com a turma)',
        'AUTOAVALIAÇÃO DOCENTE (Clareza na exposição/orientação dos conteúdos)',
        'AUTOAVALIAÇÃO DOCENTE (Assiduidade/pontualidade às atividades didáticas e de pesquisa)',
        'AUTOAVALIAÇÃO DOCENTE (Disponibilidade em ministrar componentes curriculares no mestrado)',
        'AUTOAVALIAÇÃO DOCENTE (Dedicação aos componentes ministrados)',
        'AUTOAVALIAÇÃO DOCENTE (Orientação na elaboração da Dissertação/Produto)',
        'AUTOAVALIAÇÃO DOCENTE (Tempo que disponibiliza para seus orientandos)',
        'AUTOAVALIAÇÃO DOCENTE (Interlocução entre aulas e pesquisas)',
        'AUTOAVALIAÇÃO DOCENTE (Disponilidade em compor comissões do mestrado)',
        'AUTOAVALIAÇÃO DOCENTE (Disponibilidade em colaborar em atividades diversas do mestrado que são solicitadas)'
    ]
    # Adicione outros grupos conforme necessário
}
st.set_page_config(layout="wide")

# Definir as categorias (inverter a ordem)
categorias = ['Muito Alto', 'Alto', 'Médio', 'Baixo', 'Muito Baixo', 'Não Sabe']

# Título do aplicativo
st.title("Autoavaliação PPGSC - Pesquisa docente")

# Seleção de múltiplos anos
anos_selecionados = st.multiselect("Selecione os Anos:", df['Ano'].unique(), default=df['Ano'].unique()[:1])

# Função para gerar gráficos
def gerar_grafico(selecao, titulo_grupo):
    # Filtrar os dados para os anos selecionados e a coluna de Variável de Interesse
    df_filtrado = df[df['Ano'].isin(anos_selecionados)]

    # Transformar o DataFrame em formato longo
    df_melted = pd.melt(df_filtrado, id_vars=['Ano'], value_vars=[selecao], 
                        var_name='Variável de Interesse', value_name='Categoria')

    # Contar as ocorrências de cada categoria e calcular percentuais
    contagem_df = df_melted.groupby(['Ano', 'Variável de Interesse', 'Categoria']).size().reset_index(name='Contagem')

    # Calcular percentuais dentro de cada ano
    contagem_df['Percentual'] = contagem_df.groupby(['Ano', 'Variável de Interesse'])['Contagem'].transform(lambda x: 100 * x / x.sum())

    # Configurar o gráfico
    plt.figure(figsize=(6, 4))

    # Criar o gráfico de barras com hue e definir a ordem das categorias
    sns.set(style="whitegrid")
    g = sns.barplot(
        data=contagem_df, x="Categoria", y="Percentual", hue="Ano", palette="Set1", ci=None, order=categorias
    )

        # Adicionar percentuais dentro das barras
    for p in g.patches:
        height = p.get_height()
        g.text(p.get_x() + p.get_width() / 2, height + 0.5, f'{height:.1f}%', ha="center", va="bottom", fontsize=10)

    # Alterar o fontsize das categorias no eixo x
    g.set_xticklabels(g.get_xticklabels(), fontsize=10)

    # Ajustar o título e os rótulos
    g.set_title(f"{titulo_grupo}: {selecao}", fontsize=12)
    g.set_xlabel("Avaliação", fontsize=10)
    g.set_ylabel("Percentual (%)", fontsize=10)

    # Mostrar o gráfico
    st.pyplot(plt)
    plt.close()  # Fecha a figura para evitar duplicações

# Criar uma estrutura de layout com 3 colunas (uma para cada grupo de infraestrutura)
col1, col2, col3 = st.columns([1,1,1])


# Exibir gráficos de cada grupo, permitindo a escolha da coluna de interesse
with col1:
    st.header("Infraestrutura")
    selecao_infra = st.selectbox("Selecione a variável de Infraestrutura:", grupos['INFRAESTRUTURA'])
    gerar_grafico(selecao_infra, "INFRAESTRUTURA")

with col2:
    st.header("Gestão")
    selecao_gestao = st.selectbox("Selecione a variável de Gestão:", grupos['GESTÃO'])
    gerar_grafico(selecao_gestao, "GESTÃO")

with col3:
    st.header("Avaliação dos Discentes")
    selecao_discentes = st.selectbox("Selecione a variável de Avaliação dos Discentes:", grupos['AVALIAÇÃO DOS DISCENTES'])
    gerar_grafico(selecao_discentes, "AVALIAÇÃO DOS DISCENTES")

st.write("")

col4, col5, col6 = st.columns([1,1,1])

# Exibir gráficos da segunda linha
with col4:
    if len(grupos['INFRAESTRUTURA']) > 1:
        selecao_infra = st.selectbox("Selecione a próxima variável de Infraestrutura:", grupos['INFRAESTRUTURA'][1:], key="infra2")
        gerar_grafico(selecao_infra, "INFRAESTRUTURA")

with col5:
    if len(grupos['GESTÃO']) > 1:
        selecao_gestao = st.selectbox("Selecione a próxima variável de Gestão:", grupos['GESTÃO'][1:], key="gestao2")
        gerar_grafico(selecao_gestao, "GESTÃO")

with col6:
    if len(grupos['AVALIAÇÃO DOS DISCENTES']) > 1:
        selecao_discentes = st.selectbox("Selecione a próxima variável de Avaliação dos Discentes:", grupos['AVALIAÇÃO DOS DISCENTES'][1:], key="discentes2")
        gerar_grafico(selecao_discentes, "AVALIAÇÃO DOS DISCENTES")
# with col4:
#     st.header("Dissertação")
#     selecao_discentes = st.selectbox("Selecione a variável de Dissertação:", grupos['DISSERTAÇÃO'])
#     gerar_grafico(selecao_discentes, "DISSERTAÇÃO")

# with col5:
#     st.header("Pesquisa")
#     selecao_discentes = st.selectbox("Selecione a variável de Pesquisa:", grupos['PESQUISA'])
#     gerar_grafico(selecao_discentes, "PESQUISA")

# with col6:
#     st.header("Internacionalização")
#     selecao_discentes = st.selectbox("Selecione a variável de Internacionalização:", grupos['INTERNACIONALIZAÇÃO'])
#     gerar_grafico(selecao_discentes, "INTERNACIONALIZAÇÃO")

    # streamlit run dash6.py
