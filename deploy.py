
import pandas as pd
import plotly.express as px
import streamlit as st


data = {
    'Data': ['8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54'],
    'nome': ['Marco Antonio Veloso de Castro Ferreira','Amanda dos Santos de Amorim ','Ronny Batista de sousa','Maria Cristina Pinilla Castellanos','Tainá Santos Jardim ','Wylnara dos Santos Braga','Tamyres Araújo Andrade Donato','Alessandro Martins Ribeiro','Vitória Santos Caires','1','Raisa Santos Ribeiro Cerqueira','Bárbara Emanuely de Brito Guimarães Santos','Iara Caroline Silva Machado'],
    'cpf': ['91231361700','08229426589','60577824376','08187357169','060.371.345-96 ','00060939222','03329179597','06460243530','07851143519','1','05771947555','03809117528','00845959573'],
    'nivel': ['Mestrado','Mestrado','Doutorado','Mestrado','Mestrado','Doutorado','Doutorado','Doutorado','Mestrado','1','Doutorado','Doutorado','Doutorado'],
    'faixa_etaria': ['51 a 60 anos','20 a 30 anos','20 a 30 anos','20 a 30 anos','20 a 30 anos','31 a 40 anos','31 a 40 anos','20 a 30 anos','20 a 30 anos','1','31 a 40 anos','31 a 40 anos','31 a 40 anos'],
    'idade_mestrado': ['55','24','30','28','28','32','36','28','24','1','31','34','39'],
    'sexo': ['Masculino','Feminino','Masculino','Feminino','Feminino','Feminino','Feminino','Masculino','Feminino','1','Feminino','Feminino','Feminino'],
    'orientacao_sexual': ['Heterossexual','Heterossexual','Homosexual','Heterossexual','Heterossexual','Heterossexual','Heterossexual','Homosexual','Heterossexual','1','Heterossexual','Heterossexual','Heterossexual'],
    'genero': ['Homem cis','Mulher cis','Homem cis','Mulher cis','Mulher cis','Mulher cis','','Homem cis','Mulher cis','1','Mulher cis','Mulher cis','Mulher cis'],
    'origem': ['Vitória da Conquista','Brumado','Teresina-PI','Tabio, Cundinamarca, Colombia','Vitória da Conquista','Manaus- AM','Vitória da Conquista','Porto Seguro','Barra da Estiva','1','Poções','Vitória da Conquista','Vitória da Conquista'],
    'cor': ['Parda','Branca','Preta','Branca','Parda','Parda','Branca','Branca','Parda','1','Branca','Parda','Parda'],
    'Estado Civil': ['Casado (a)','Casado (a)','Em relacionamento estável','Solteiro (a)','Solteiro (a)','Casado (a)','Casado (a)','Solteiro (a)','Casado (a)','1','Casado (a)','Casado (a)','Casado (a)'],
    'Curso de Graduação': ['Medicina','Biomedicina ','Assistência Social','Saúde Coletiva','Farmácia ','Serviço Social','Enfermangem','Biomedicina','Nutrição','1','Nutrição','Psicologia','Enfermangem'],
    'Tipo de instituição em que realizou a graduação': ['Universidade Pública Federal','Universidade Privada','Universidade Privada','Universidade Pública Federal','Universidade Privada','Universidade Pública Federal','Universidade Pública Estadual','Universidade Privada','Universidade Pública Federal','1','Universidade Pública Federal','Universidade Pública Federal','Universidade Privada'],
    'Ano de conclusão da graduação': ['1996','12/2021; colação de grau em 03/2022','2017','2022','2023','2013','2011','2019','2023','1','2017','2016','2009'],
    'É bolsista no PPGSC?': ['Não','Sim','Sim','Sim','Não','Não','Não','Sim','Sim','1','Sim','Não','Sim'],
    'Qual a agência que financia?': ['','FAPESB','FAPESB','CAPES','','','','FAPESB','CAPES','1','CAPES','','FAPESB'],
    'O processo seletivo': ['Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','1','Muito satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)'],
    'O ingresso no Programa': ['Muito satisfatório (a)','Muito satisfatório (a)','Muito insatisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','1','Muito satisfatório (a)','Muito satisfatório (a)','Muito insatisfatório (a)'],
    'O processo de recepção/direcionamento de novos alunos': ['Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','1','Muito satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)'],
    'Adequação dos componentes curriculares do curso (quantidade, duração) aos objetivos da formação pretendida.': ['Muito satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Insatisfatório (a)','Muito satisfatório (a)','1','Satisfatório (a)','Muito satisfatório (a)','Neutro'],
    'Relação do conteúdo e atividades nas aulas com os objetivos da formação pretendida.': ['Muito satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','1','Satisfatório (a)','Muito satisfatório (a)','Insatisfatório (a)'],
    'As atividades acadêmicas desenvolvem as habilidades necessárias para o exercício profissional.': ['Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','1','Muito satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)'],
    'Equilíbrio entre componentes obrigatórios, optativos e o desenvolvimento da dissertação/tese.': ['Muito satisfatório (a)','Satisfatório (a)','Neutro','Neutro','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Neutro','Muito satisfatório (a)','1','Satisfatório (a)','Muito satisfatório (a)','Neutro'],
    'Nível de desenvolvimento de aprendizagens e competências para o ensino.': ['Muito satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','1','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)'],
    'Nível de desenvolvimento de aprendizagens e competências para a pesquisa.': ['Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','1','Satisfatório (a)','Muito satisfatório (a)','Neutro'],
    'Nível de desenvolvimento de aprendizagens e competências para a atividade profissional.': ['Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Neutro','Muito satisfatório (a)','1','Satisfatório (a)','Muito satisfatório (a)','Neutro'],
    'Participação em eventos científicos nacionais ou internacionais.': ['Satisfatório (a)','Neutro','Muito insatisfatório (a)','Neutro','Satisfatório (a)','Neutro','Satisfatório (a)','Neutro','Neutro','1','Insatisfatório (a)','Satisfatório (a)','Muito insatisfatório (a)'],
    'Produção de artigos científicos e/ou capítulos de livros para publicação.': ['Neutro','Satisfatório (a)','Muito insatisfatório (a)','Neutro','Muito satisfatório (a)','Neutro','Satisfatório (a)','Neutro','Satisfatório (a)','1','Satisfatório (a)','Satisfatório (a)','Neutro'],
    'Participação nas atividades do grupo de pesquisa.': ['Neutro','Neutro','Muito insatisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Neutro','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','1','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)'],
    'Participação em projetos de extensão.': ['Neutro','Satisfatório (a)','Muito insatisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Neutro','Neutro','Satisfatório (a)','Muito satisfatório (a)','1','Neutro','Satisfatório (a)','Neutro'],
    'Intercâmbios com outros programas nacionais': ['Insatisfatório (a)','Neutro','Insatisfatório (a)','Neutro','Muito satisfatório (a)','Neutro','Neutro','Neutro','Satisfatório (a)','1','Insatisfatório (a)','Neutro','Neutro'],
    'Intercâmbios com outros programas internacionais': ['Insatisfatório (a)','Neutro','Insatisfatório (a)','Neutro','Muito satisfatório (a)','Neutro','Neutro','Neutro','Neutro','1','Insatisfatório (a)','Neutro','Neutro'],
    'Instalações física/tecnológica': ['Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','1','Muito satisfatório (a)','Satisfatório (a)','Insatisfatório (a)'],
    'As salas de aula, salas de grupos de pesquisa': ['Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','1','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)'],
    'O acesso à biblioteca ou às bases de dados necessárias': ['Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Neutro','Muito satisfatório (a)','Insatisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','1','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)'],
    'As condições dos laboratórios de pesquisa (espaços, equipamentos, materiais necessários)': ['Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Neutro','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','1','Muito satisfatório (a)','Neutro','Satisfatório (a)'],
    'A secretaria (pessoal e instalações) ': ['Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Neutro','Muito satisfatório (a)','Neutro','Muito satisfatório (a)','Neutro','Muito satisfatório (a)','1','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)'],
    'Acesso às plataformas remotas': ['Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Neutro','Muito satisfatório (a)','Neutro','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','1','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)'],
    'Desempenho da Coordenação': ['Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','1','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)'],
    'Desempenho de setores de apoio (Secretaria, laboratórios)': ['Muito satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Neutro','Muito satisfatório (a)','Neutro','Muito satisfatório (a)','Neutro','Muito satisfatório (a)','1','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)'],
    'A competência técnica (habilidade em desenvolver as aulas e demonstrar o domínio dos conteúdos da disciplina no ensino presencial). ': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'A competência relacional (capacidade em se relacionar com os alunos e propiciar um clima adequado para a aprendizagem no ensino presencial).': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente'],
    'A competência didática (capacidade de transmitir conteúdos; organizar as atividades de aprendizagem, avaliar o processo de ensino-aprendizagem no ensino presencial).': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente'],
    'O compromisso (atenção aos alunos e disposição para cumprir o planejamento apresentado no início do semestre presencial).': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Concluir esta pós-graduação é uma parte fundamental dos meus planos de carreira.': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Neste programa de pós-graduação, tenho feito amizades que contribuem para o meu crescimento pessoal.': ['Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'O relacionamento com os professores tem contribuído para o meu crescimento pessoal.': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Sinto-me à vontade para iniciar conversação com os professores e coordenadores do meu programa.': ['Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'As disciplinas e as atividades que estamos realizando têm sido estimulantes intelectualmente.': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Eu estou altamente comprometido em obter o meu diploma nesta pós-graduação.': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Nesta universidade, tenho feito amizades que contribuem para o meu crescimento intelectual.': ['Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente'],
    'Estou satisfeito com a qualidade dos professores da minha pós-graduação.': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Tenho pensado seriamente em desistir minha pós-graduação.': ['Discordo Totalmente','Discordo Totalmente','Discordo Totalmente','Discordo Totalmente','Concordo Totalmente','Neutro','Discordo Totalmente','Discordo Totalmente','Discordo Totalmente','1','Discordo Totalmente','Discordo Totalmente','Discordo Totalmente'],
    'Eu gosto das conversas que eu tenho com os meus colegas da pós-graduação.': ['Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Discordo Parcialmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente'],
    'O relacionamento com os professores tem contribuído para o meu crescimento intelectual.': ['Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Percebo que o que estou aprendendo na pós-graduação é fundamental para o trabalho na carreira que escolhi': ['Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Completar esta pós-graduação é uma meta de vida para mim.': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Eu gosto de ter atividades sociais com os meus colegas de universidade.': ['Concordo Totalmente','Concordo Parcialmente','Neutro','Concordo Totalmente','Concordo Totalmente','Discordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Neutro'],
    'O contato com professores ou coordenações acadêmicas têm auxiliado nas minhas reflexões sobre a carreira profissional.': ['Concordo Totalmente','Concordo Parcialmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Neutro','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Sinto que através das disciplinas estou desenvolvendo as habilidades necessárias para o exercício profissional': ['Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente'],
    'As pressões que vivo para realizar a pós-graduação afetam o meu bem estar físico.': ['Discordo Parcialmente','Discordo Parcialmente','Concordo Parcialmente','Neutro','Concordo Totalmente','Concordo Totalmente','Neutro','Discordo Parcialmente','Neutro','1','Concordo Parcialmente','Discordo Totalmente','Concordo Parcialmente'],
    'As pressões que vivo para realizar a pós-graduação afetam o meu bem estar psicológico.': ['Discordo Parcialmente','Discordo Totalmente','Concordo Parcialmente','Neutro','Concordo Totalmente','Concordo Totalmente','Neutro','Concordo Parcialmente','Neutro','1','Concordo Parcialmente','Discordo Totalmente','Concordo Parcialmente'],
    'Não tenho tido tempo para estudar e cumprir as demandas da pós-graduação': ['Discordo Totalmente','Discordo Totalmente','Neutro','Neutro','Concordo Totalmente','Neutro','Discordo Parcialmente','Discordo Parcialmente','Neutro','1','Discordo Totalmente','Discordo Totalmente','Discordo Parcialmente'],
    'A quantidade de tarefas acadêmicas (leituras, exercícios, trabalhos) é excessiva para mim.': ['Discordo Totalmente','Discordo Parcialmente','Concordo Parcialmente','Concordo Parcialmente','Concordo Totalmente','Concordo Parcialmente','Concordo Parcialmente','Neutro','Neutro','1','Concordo Parcialmente','Discordo Totalmente','Neutro'],
    'Minha carga de trabalho aumentou (em casa e/ou fora de casa)': ['Discordo Totalmente','Neutro','Neutro','Concordo Parcialmente','Concordo Totalmente','Neutro','Concordo Parcialmente','Neutro','Neutro','1','Concordo Parcialmente','Concordo Parcialmente','Concordo Parcialmente'],
    'Contribuir para a melhoria da minha renda': ['Neutro','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Contribuir para a minha empregabilidade': ['Neutro','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Neutro','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Contribuir para o meu crescimento profissional': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Me capacitar para exercer a docência no ensino superior na minha área': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Neutro','Concordo Totalmente','Neutro','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Me capacitar para conceber e desenvolver projetos de pesquisas no meu campo de conhecimento': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Ampliar a minha capacitação para atuar profissionalmente na minha área': ['Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Ampliar a minha capacitação para conceber e desenvolver projetos de extensão e serviços para segmentos da sociedade': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente']
}


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
]

# Título do aplicativo
st.title("Autoavaliação - Egressos")

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

# Criar o gráfico de barras com Plotly Express
fig = px.bar(
    contagem_df,
    x="Categoria",
    y="Contagem",
    color="Ano",
    barmode='group',
    title=f"Avaliação dos docentes para {infra_selecionada}",
    labels={"Categoria": "Avaliação", "Contagem": "Frequência"},
)

# Mostrar o gráfico no Streamlit
st.plotly_chart(fig)
