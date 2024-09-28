
import pandas
import matplotlib.pyplot
import seaborn
import streamlit


data = {
    'Data': ['8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54','8/9/24 15:50:54'],
    'nome': ['Marco Antonio Veloso de Castreamlitro Ferreira','Amanda dos Santos de Amorim ','Ronny Batistreamlita de sousa','Maria Cristreamlitina Pinilla Castreamlitellanos','Tainá Santos Jardim ','Wylnara dos Santos Braga','Tamyres Araújo Andrade Donato','Alessandro Martins Ribeiro','Vitória Santos Caires','1','Raisa Santos Ribeiro Cerqueira','Bárbara Emanuely de Brito Guimarães Santos','Iara Caroline Silva Machado'],
    'cpf': ['91231361700','08229426589','60577824376','08187357169','060.371.345-96 ','00060939222','03329179597','06460243530','07851143519','1','05771947555','03809117528','00845959573'],
    'nivel': ['Mestreamlitrado','Mestreamlitrado','Doutorado','Mestreamlitrado','Mestreamlitrado','Doutorado','Doutorado','Doutorado','Mestreamlitrado','1','Doutorado','Doutorado','Doutorado'],
    'faixa_etaria': ['51 a 60 anos','20 a 30 anos','20 a 30 anos','20 a 30 anos','20 a 30 anos','31 a 40 anos','31 a 40 anos','20 a 30 anos','20 a 30 anos','1','31 a 40 anos','31 a 40 anos','31 a 40 anos'],
    'idade_mestreamlitrado': ['55','24','30','28','28','32','36','28','24','1','31','34','39'],
    'sexo': ['Masculino','Feminino','Masculino','Feminino','Feminino','Feminino','Feminino','Masculino','Feminino','1','Feminino','Feminino','Feminino'],
    'orientacao_sexual': ['Heterossexual','Heterossexual','Homosexual','Heterossexual','Heterossexual','Heterossexual','Heterossexual','Homosexual','Heterossexual','1','Heterossexual','Heterossexual','Heterossexual'],
    'genero': ['Homem cis','Mulher cis','Homem cis','Mulher cis','Mulher cis','Mulher cis','','Homem cis','Mulher cis','1','Mulher cis','Mulher cis','Mulher cis'],
    'origem': ['Vitória da Conquistreamlita','Brumado','Teresina-PI','Tabio, Cundinamarca, Colombia','Vitória da Conquistreamlita','Manaus- AM','Vitória da Conquistreamlita','Porto Seguro','Barra da Estreamlitiva','1','Poções','Vitória da Conquistreamlita','Vitória da Conquistreamlita'],
    'cor': ['Parda','Branca','Preta','Branca','Parda','Parda','Branca','Branca','Parda','1','Branca','Parda','Parda'],
    'Estreamlitado Civil': ['Casado (a)','Casado (a)','Em relacionamento estreamlitável','Solteiro (a)','Solteiro (a)','Casado (a)','Casado (a)','Solteiro (a)','Casado (a)','1','Casado (a)','Casado (a)','Casado (a)'],
    'Curso de Graduação': ['Medicina','Biomedicina ','Assistreamlitência Social','Saúde Coletiva','Farmácia ','Serviço Social','Enfermangem','Biomedicina','Nutrição','1','Nutrição','Psicologia','Enfermangem'],
    'Tipo de instreamlitituição em que realizou a graduação': ['Universidade Pública Federal','Universidade Privada','Universidade Privada','Universidade Pública Federal','Universidade Privada','Universidade Pública Federal','Universidade Pública Estreamlitadual','Universidade Privada','Universidade Pública Federal','1','Universidade Pública Federal','Universidade Pública Federal','Universidade Privada'],
    'Ano de conclusão da graduação': ['1996','12/2021; colação de grau em 03/2022','2017','2022','2023','2013','2011','2019','2023','1','2017','2016','2009'],
    'É bolsistreamlita no PPGSC?': ['Não','Sim','Sim','Sim','Não','Não','Não','Sim','Sim','1','Sim','Não','Sim'],
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
    'Instreamlitalações física/tecnológica': ['Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','1','Muito satisfatório (a)','Satisfatório (a)','Insatisfatório (a)'],
    'As salas de aula, salas de grupos de pesquisa': ['Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','1','Muito satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)'],
    'O acesso à biblioteca ou às bases de dados necessárias': ['Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Neutro','Muito satisfatório (a)','Insatisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','1','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)'],
    'As condições dos laboratórios de pesquisa (espaços, equipamentos, materiais necessários)': ['Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Neutro','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','1','Muito satisfatório (a)','Neutro','Satisfatório (a)'],
    'A secretaria (pessoal e instreamlitalações) ': ['Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Neutro','Muito satisfatório (a)','Neutro','Muito satisfatório (a)','Neutro','Muito satisfatório (a)','1','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)'],
    'Acesso às plataformas remotas': ['Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Neutro','Muito satisfatório (a)','Neutro','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','1','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)'],
    'Desempenho da Coordenação': ['Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)','1','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)'],
    'Desempenho de setores de apoio (Secretaria, laboratórios)': ['Muito satisfatório (a)','Muito satisfatório (a)','Satisfatório (a)','Neutro','Muito satisfatório (a)','Neutro','Muito satisfatório (a)','Neutro','Muito satisfatório (a)','1','Muito satisfatório (a)','Muito satisfatório (a)','Muito satisfatório (a)'],
    'A competência técnica (habilidade em desenvolver as aulas e demonstreamlitrar o domínio dos conteúdos da disciplina no ensino presencial). ': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'A competência relacional (capacidade em se relacionar com os alunos e propiciar um clima adequado para a aprendizagem no ensino presencial).': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente'],
    'A competência didática (capacidade de transmitir conteúdos; organizar as atividades de aprendizagem, avaliar o processo de ensino-aprendizagem no ensino presencial).': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente'],
    'O compromisso (atenção aos alunos e disposição para cumprir o planejamento apresentado no início do semestreamlitre presencial).': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Concluir estreamlita pós-graduação é uma parte fundamental dos meus planos de carreira.': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Nestreamlite programa de pós-graduação, tenho feito amizades que contribuem para o meu crescimento pessoal.': ['Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'O relacionamento com os professores tem contribuído para o meu crescimento pessoal.': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Sinto-me à vontade para iniciar conversação com os professores e coordenadores do meu programa.': ['Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'As disciplinas e as atividades que estreamlitamos realizando têm sido estreamlitimulantes intelectualmente.': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Eu estreamlitou altamente comprometido em obter o meu diploma nestreamlita pós-graduação.': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Nestreamlita universidade, tenho feito amizades que contribuem para o meu crescimento intelectual.': ['Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente'],
    'Estreamlitou satisfeito com a qualidade dos professores da minha pós-graduação.': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Tenho pensado seriamente em desistreamlitir minha pós-graduação.': ['Discordo Totalmente','Discordo Totalmente','Discordo Totalmente','Discordo Totalmente','Concordo Totalmente','Neutro','Discordo Totalmente','Discordo Totalmente','Discordo Totalmente','1','Discordo Totalmente','Discordo Totalmente','Discordo Totalmente'],
    'Eu gostreamlito das conversas que eu tenho com os meus colegas da pós-graduação.': ['Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Discordo Parcialmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente'],
    'O relacionamento com os professores tem contribuído para o meu crescimento intelectual.': ['Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Percebo que o que estreamlitou aprendendo na pós-graduação é fundamental para o trabalho na carreira que escolhi': ['Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Completar estreamlita pós-graduação é uma meta de vida para mim.': ['Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Eu gostreamlito de ter atividades sociais com os meus colegas de universidade.': ['Concordo Totalmente','Concordo Parcialmente','Neutro','Concordo Totalmente','Concordo Totalmente','Discordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Neutro'],
    'O contato com professores ou coordenações acadêmicas têm auxiliado nas minhas reflexões sobre a carreira profissional.': ['Concordo Totalmente','Concordo Parcialmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Neutro','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente'],
    'Sinto que através das disciplinas estreamlitou desenvolvendo as habilidades necessárias para o exercício profissional': ['Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente','Concordo Totalmente','1','Concordo Totalmente','Concordo Totalmente','Concordo Parcialmente'],
    'As pressões que vivo para realizar a pós-graduação afetam o meu bem estreamlitar físico.': ['Discordo Parcialmente','Discordo Parcialmente','Concordo Parcialmente','Neutro','Concordo Totalmente','Concordo Totalmente','Neutro','Discordo Parcialmente','Neutro','1','Concordo Parcialmente','Discordo Totalmente','Concordo Parcialmente'],
    'As pressões que vivo para realizar a pós-graduação afetam o meu bem estreamlitar psicológico.': ['Discordo Parcialmente','Discordo Totalmente','Concordo Parcialmente','Neutro','Concordo Totalmente','Concordo Totalmente','Neutro','Concordo Parcialmente','Neutro','1','Concordo Parcialmente','Discordo Totalmente','Concordo Parcialmente'],
    'Não tenho tido tempo para estreamlitudar e cumprir as demandas da pós-graduação': ['Discordo Totalmente','Discordo Totalmente','Neutro','Neutro','Concordo Totalmente','Neutro','Discordo Parcialmente','Discordo Parcialmente','Neutro','1','Discordo Totalmente','Discordo Totalmente','Discordo Parcialmente'],
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

df = pandas.DataFrame(data)

print(df['Data'].unique())

df.head()

df['Date'] = pandas.to_datetime(df['Data'])
# Extraindo o ano para facilitar a filtragem depois
df['Ano'] = df['Date'].dt.year




# Definir as colunas de infraestreamlitrutura
colunas = ['nivel',
    'faixa_etaria',
    'idade_mestreamlitrado',
    'sexo',
    'orientacao_sexual',
    'genero',
    'origem',
    'cor',
    'Estreamlitado Civil',
    'Curso de Graduação',
    'Tipo de instreamlitituição em que realizou a graduação',
    'Ano de conclusão da graduação',
    'É bolsistreamlita no PPGSC?',
    'Qual a agência que financia?',
    'O processo seletivo',
    'O ingresso no Programa',
    'O processo de recepção/direcionamento de novos alunos',
    'Adequação dos componentes curriculares do curso (quantidade, duração) aos objetivos da formação pretendida.',
    'Relação do conteúdo e atividades nas aulas com os objetivos da formação pretendida.',
    'As atividades acadêmicas desenvolvem as habilidades necessárias para o exercício profissional.',
    'Equilíbrio entre componentes obrigatórios, optativos e o desenvolvimento da dissertação/tese.',
    'Nível de desenvolvimento de aprendizagens e competências para o ensino.',
    'Nível de desenvolvimento de aprendizagens e competências para a pesquisa.',
    'Nível de desenvolvimento de aprendizagens e competências para a atividade profissional.',
    'Participação em eventos científicos nacionais ou internacionais.',
    'Produção de artigos científicos e/ou capítulos de livros para publicação.',
    'Participação nas atividades do grupo de pesquisa.',
    'Participação em projetos de extensão.',
    'Intercâmbios com outros programas nacionais',
    'Intercâmbios com outros programas internacionais',
    'Instreamlitalações física/tecnológica',
    'As salas de aula, salas de grupos de pesquisa',
    'O acesso à biblioteca ou às bases de dados necessárias',
    'As condições dos laboratórios de pesquisa (espaços, equipamentos, materiais necessários)',
    'A secretaria (pessoal e instreamlitalações) ',
    'Acesso às plataformas remotas',
    'Desempenho da Coordenação',
    'Desempenho de setores de apoio (Secretaria, laboratórios)',
    'A competência técnica (habilidade em desenvolver as aulas e demonstreamlitrar o domínio dos conteúdos da disciplina no ensino presencial). ',
    'A competência relacional (capacidade em se relacionar com os alunos e propiciar um clima adequado para a aprendizagem no ensino presencial).',
    'A competência didática (capacidade de transmitir conteúdos; organizar as atividades de aprendizagem, avaliar o processo de ensino-aprendizagem no ensino presencial).',
    'O compromisso (atenção aos alunos e disposição para cumprir o planejamento apresentado no início do semestreamlitre presencial).',
    'Concluir estreamlita pós-graduação é uma parte fundamental dos meus planos de carreira.',
    'Nestreamlite programa de pós-graduação, tenho feito amizades que contribuem para o meu crescimento pessoal.',
    'O relacionamento com os professores tem contribuído para o meu crescimento pessoal.',
    'Sinto-me à vontade para iniciar conversação com os professores e coordenadores do meu programa.',
    'As disciplinas e as atividades que estreamlitamos realizando têm sido estreamlitimulantes intelectualmente.',
    'Eu estreamlitou altamente comprometido em obter o meu diploma nestreamlita pós-graduação.',
    'Nestreamlita universidade, tenho feito amizades que contribuem para o meu crescimento intelectual.',
    'Estreamlitou satisfeito com a qualidade dos professores da minha pós-graduação.',
    'Tenho pensado seriamente em desistreamlitir minha pós-graduação.',
    'Eu gostreamlito das conversas que eu tenho com os meus colegas da pós-graduação.',
    'O relacionamento com os professores tem contribuído para o meu crescimento intelectual.',
    'Percebo que o que estreamlitou aprendendo na pós-graduação é fundamental para o trabalho na carreira que escolhi',
    'Completar estreamlita pós-graduação é uma meta de vida para mim.',
    'Eu gostreamlito de ter atividades sociais com os meus colegas de universidade.',
    'O contato com professores ou coordenações acadêmicas têm auxiliado nas minhas reflexões sobre a carreira profissional.',
    'Sinto que através das disciplinas estreamlitou desenvolvendo as habilidades necessárias para o exercício profissional',
    'As pressões que vivo para realizar a pós-graduação afetam o meu bem estreamlitar físico.',
    'As pressões que vivo para realizar a pós-graduação afetam o meu bem estreamlitar psicológico.',
    'Não tenho tido tempo para estreamlitudar e cumprir as demandas da pós-graduação',
    'A quantidade de tarefas acadêmicas (leituras, exercícios, trabalhos) é excessiva para mim.',
    'Minha carga de trabalho aumentou (em casa e/ou fora de casa)',
    'Contribuir para a melhoria da minha renda',
    'Contribuir para a minha empregabilidade',
    'Contribuir para o meu crescimento profissional',
    'Me capacitar para exercer a docência no ensino superior na minha área',
    'Me capacitar para conceber e desenvolver projetos de pesquisas no meu campo de conhecimento',
    'Ampliar a minha capacitação para atuar profissionalmente na minha área',
    'Ampliar a minha capacitação para conceber e desenvolver projetos de extensão e serviços para segmentos da sociedade'
    ]  # Adicione todas as colunas de infraestreamlitrutura aqui


# Título do aplicativo
streamlit.title("Autoavaliação PPGSC - Pesquisa docente")

# Seleção de múltiplos anos
periodo = streamlit.multiselect("Selecione os Anos:", df['Ano'].unique(), default=df['Ano'].unique()[:2])

# Seleção da coluna de infraestreamlitrutura
variavel = streamlit.selectbox("Selecione a Coluna", colunas, key="selectbox_infra")

# Filtrar os dados para os anos selecionados e a coluna de infraestreamlitrutura
df_filtrado = df[df['Ano'].isin(periodo)]

# Transformar o DataFrame em formato longo
df_melted = pandas.melt(df_filtrado, id_vars=['Ano'], value_vars=[variavel], 
                    var_name='Infraestreamlitrutura', value_name='Categoria')

# Contar as ocorrências de cada categoria
contagem_df = df_melted.groupby(['Ano', 'Infraestreamlitrutura', 'Categoria']).size().reset_index(name='Contagem')

# Configurar o gráfico
matplotlib.pyplot.figure(figsize=(12, 8))

# Criar o gráfico de barras com hue
seaborn.set(streamlityle="whitegrid")
g = seaborn.barplot(
    data=contagem_df, x="Categoria", y="Contagem", hue="Ano", palette="Set1", ci=None
)

# Ajustreamlitar o título e os rótulos
g.set_title(f"Avaliação dos docentes para {variavel}", fontsize = 16)
g.set_xlabel("Avaliação")
g.set_ylabel("Frequência")

# Mostreamlitrar o gráfico no streamlitreamlit
streamlit.pyplot(matplotlib.pyplot)

matplotlib.pyplot.close()  # Fecha a figura para evitar duplicações

# streamlitreamlit run deploy.py
