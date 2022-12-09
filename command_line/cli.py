import click
import pyfiglet
import requests
from .config import *
from .extractor import GTExtract
import sys


try:
    c = GTExtract()
except Exception:
    pass


@click.group(options_metavar='<OPTIONS>')
@click.version_option(version="v1.0.5", help="Shows the Version", message="GITURLGETTER, Version: %(version)s")
@click.help_option("-h", "--help", help="To Get Help")
def main():
    """Giturlgetter CLI to extract the Repository clone url.
        Also it can extract the Repository Details\n
        """
    pass


def createfile(token, uname):
    with open(f"{PATH}\config.env", 'w') as f:
        f.write(f"token={token}\nuname={uname}")


def getrequired():
    res = requests.get(
        f"https://api.jsonbin.io/v3/b/{BIN_ID}?meta=false", headers={"X-Access-Key": JSON_API}).json()
    return res['client_id'], res['client_secrets']


def verifylogin():
    if TOKEN_INSERTED:
        pass
    else:
        click.echo(
            f"Login First to Proceed\nUse {click.style('giturl login',fg='bright_yellow',underline=True,bold=True)} Command")
        sys.exit(0)


def printurls(id_name):
    url_container = c.getrepourl(id_name)
    if not url_container:
        click.secho("Id or Name is Incorrect", bg="bright_green", fg="black")
        click.echo(
            f"Use Command {click.style('giturl list',fg='bright_white',bold=True)} To get ID and name")
    else:
        for u in url_container:
            click.echo(f"{click.style(u[0],fg='bright_cyan')} : {u[1]}")


def printrepolist(uname):
    repository_list = c.getlist(uname)
    if repository_list == False:
        click.echo("Username Not Found")
    else:
        click.echo(
            f'{click.style("ID",fg="bright_yellow",underline=True)} \t  | {click.style("Repo Name",fg="bright_yellow",underline=True)}')
        for a in c.getlist(uname):
            id, name = a
            click.echo_via_pager(f"{id} | {name}")


def printuserDetails(uname):
    det = c.details(uname)
    if det is None:
        click.secho("Invalid Username ❕", fg="bright_red")
    else:
        for o in det:
            click.echo(f"{click.style(o[0],fg='bright_cyan')} : {o[1]}")


@main.command(name="login", help="Login via Github", add_help_option=True, options_metavar="<OPTION>")
@click.help_option("-h", "--help", help="To Get Help")
def logon():
    """Login via Github """
    if TOKEN_INSERTED:
        click.echo("You have Already Verified ✓")
    else:
        try:
            id, secret = getrequired()
            res = requests.post(f"https://github.com/login/device/code?client_id={id}", headers={
                                'Accept': "application/json"}).json()
            click.echo(
                f"""Enter The Code in browser to verify : {click.style(res['user_code'],fg="bright_white",bold=True)}""")
            click.pause(info="Press Enter to open Github in Browser...")
            click.launch(res["verification_uri"])
            conf = click.confirm(text="Have You entered the Code ")
            if conf:
                test = requests.get(f'https://github.com/login/oauth/access_token?client_id={id}&device_code={res["device_code"]}&grant_type=urn:ietf:params:oauth:grant-type:device_code', headers={
                                    'Accept': "application/json"}).json()
                if 'access_token' in test:
                    click.echo(
                        f'{click.style("Successfully Verified",fg="bright_green")} ✓')
                    uname = requests.get("https://api.github.com/user", headers={
                                         "Authorization": f"Bearer {test['access_token']}", "Accept": "application/json"}).json()
                    createfile(test['access_token'], uname['login'])
                else:
                    click.echo(click.style(
                        "Try the Command Again!!", fg="red"))
            else:
                click.echo(click.style("Try the Command Again!!", fg="red"))
        except requests.ConnectionError:
            click.echo(click.style(
                "Internet Connection Required", fg="bright_blue"))


@main.command(name="logout", help="Logout from the Github")
@click.help_option("-h", "--help", help="To Get Help")
def logout():
    """Logouts from the Github"""
    if TOKEN_INSERTED:
        confirm = click.confirm("Are You sure You want to Logout")
        if confirm:
            os.remove(f"{PATH}\config.env")
            click.echo("Successfully Logged Out")
    else:
        click.echo("You have not Logged Yet")


@main.command(name="figlet", help="Print the name in Figlet type")
@click.help_option("-h", "--help", help="To Get Help")
def figlet():
    """To print The Giturlgetter in figlet type"""
    text = pyfiglet.figlet_format("GITURLGETTER")
    click.echo(f"{text}")


@main.command(name="list", help="Lists the Repository of the user", options_metavar="<option>")
@click.option("--default", help="Lists the Repository of the user", is_flag=True, flag_value=True)
@click.argument("username", required=False, type=str)
@click.help_option("-h", "--help", help="To Get Help")
def lister(default, username):
    """Lists the Repository name with id --default will give user repos."""
    verifylogin()
    if default and username is None:
        printrepolist(UNAME)
    elif username is not None:
        printrepolist(username)
    else:
        auname = click.prompt("Enter the Username Default :",
                              default=UNAME, show_default=True)
        printrepolist(auname)


@main.command(name="repo", help="Shows and copies the repository clone url", options_metavar="<option>")
@click.option("-id", "--id", help="Extract the Clone url based on Repository ID", type=click.STRING, required=False)
@click.option("-n", "--name", help="Extract the Clone url based on Repository Name", type=click.STRING, required=False)
@click.help_option("-h", "--help", help="To Get Help")
def repos(id, name):
    verifylogin()
    if id is None and name is None:
        repodet = click.prompt("Enter The Repo Id or Name ")
        try:
            id_ex = int(repodet)
            printurls(id_ex)
        except ValueError:
            printurls(repodet)
    else:
        if id is None:
            printurls(name)
        elif name is None:
            try:
                printurls(int(id))
            except ValueError:
                click.secho("Id is Incorrect", bg="bright_green", fg="black")
                click.echo(
                    f"Use Command {click.style('giturl list',fg='bright_white',bold=True)} To get correct ID")


@main.command(name="details", help="Shows the User Details", options_metavar="<option>")
@click.argument("username", required=False, type=str)
@click.help_option("-h", "--help", help="To Get Help")
def details(username):
    verifylogin()
    if username is None:
        uname = click.prompt(
            "Enter the Github Username\nPress Enter To Skip Default:", default=UNAME, show_default=True)
        printuserDetails(uname)
    else:
        printuserDetails(username)
