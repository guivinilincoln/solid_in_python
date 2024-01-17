from github.client import GithubClient
from repo.parser import RepoParser
from repo.reports_generator import ReportsGenerator
from reports.html_generator import HTMLGenerator
from reports.markdown_generator import MarkdownGenerator

if __name__ == "__main__":
    username = 'guilhermelincoln'
    response = GithubClient.get_repos_by_user(username)
    
    if response['status_code'] == 200:
        print('Success !')
        repos = RepoParser.parse(response['body'])
        markdown_report = ReportsGenerator.bulid(MarkdownGenerator, repos)
        html_report = ReportsGenerator.bulid(HTMLGenerator, repos)
        
        print(markdown_report)
        print(html_report)
    else:
        print(response['body'])    
        