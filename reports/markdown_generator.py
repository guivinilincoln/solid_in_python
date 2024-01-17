class MarkdownGenerator():
    @classmethod
    def build(cls, repos):
        items = ' '.join(f'**ID:*** {repo.id} ' 
                         f'**NOME:*** {repo.name} ' 
                         f'STARS: {repo.stars} \n'
                         for repo in repos)
        return f'## REPOS \n\n {items}'