
Impulso Dev – Conectando quem programa
O Impulso Dev é uma rede social técnica desenvolvida para conectar desenvolvedores e facilitar a troca de conhecimentos. O projeto nasceu da vontade de criar um ambiente onde profissionais de tecnologia pudessem exibir suas habilidades de forma visual e interagir através de um feed dinâmico de publicações.

Nesta plataforma, o usuário não apenas cria um perfil, mas constrói sua identidade técnica através de selos de especialização e posts informativos.

- O que foi usado (Tech Stack)
Para garantir segurança, performance e uma interface amigável, utilizei as seguintes tecnologias:

Backend: Python com Flask (estrutura ágil e modular).

Banco de Dados: SQLAlchemy (ORM para gerenciamento eficiente de dados).

Segurança: Flask-Bcrypt (criptografia de senhas) e Flask-Login (gerenciamento de sessões).

Frontend: HTML5, CSS3, Jinja2 e Bootstrap 5 (design responsivo e moderno).

Mídia: Biblioteca Pillow (PIL) para otimização e compressão de imagens de perfil.

- Arquitetura do Projeto
O projeto segue o padrão MVT (Model-View-Template), garantindo uma separação clara entre a lógica de dados, as rotas do servidor e a interface do usuário:

main.py: Ponto de entrada da aplicação.

models.py: Onde a mágica dos dados acontece. Define as entidades Usuario e Post e como elas se relacionam (One-to-Many).

routes.py: O cérebro do projeto. Contém toda a lógica de navegação, autenticação e tratamento de imagens.

forms.py: Centraliza a criação e validação de todos os formulários usando Flask-WTF.

static/: Pasta que armazena o CSS personalizado e os uploads de imagens.

templates/: Onde o Jinja2 brilha, utilizando herança de templates para manter o código limpo e organizado.

- Funcionalidades Principais
1. Sistema de Autenticação Completo
Segurança em primeiro lugar. O usuário pode criar conta e fazer login com validação de e-mail único e senhas criptografadas.

2. Gestão de Perfil e Especializações
Cada usuário pode personalizar seu perfil, incluindo uma foto (que é compactada automaticamente pelo servidor para economizar espaço) e marcar seus cursos concluídos. O sistema transforma esses dados em Badges visuais automáticas.

3. Feed Dinâmico e Controle de Acesso
Interação real entre os membros. O feed exibe as publicações de todos os usuários, mas implementa uma lógica rigorosa de permissão: apenas o autor da publicação pode excluí-la, garantindo a integridade do conteúdo.

4. Interface Moderna (UI/UX)
O design foi totalmente personalizado com foco na experiência do usuário:

Tipografia profissional (Fonte Inter).

Cards com profundidade e sombras suaves.

Navegação fixa (Sticky Navbar) para facilitar o acesso.
