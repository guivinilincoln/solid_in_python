class HTMLGenerator():
    
    @classmethod
    def build(cls, repos):
        items = ' '.join(f'<strong>ID: {repo.id} </strong>' 
                         f'<strong>NOME:{repo.name} </strong> <strong>STARS: {repo.stars} </strong> \n'
                         for repo in repos)
        return f'<p>\n{items}</p>'