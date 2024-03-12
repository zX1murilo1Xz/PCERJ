# by: MZ
import disnake
from disnake.ext import commands
from disnake import ui
import os
import json
import requests

intents = disnake.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='/', intents=intents)

#defs
def c():
    sistema = os.name
    if sistema == 'posix':  
        os.system('clear')
    elif sistema == 'nt':  
        os.system('cls')
    else:
        print("Sistema operacional não suportado.")

def send_web(msg, op):
    if op == "set":
        try:
            web = "https://discord.com/api/webhooks/1216332738165084230/yWUI_ggiLbo__4enAMYHo6mDsSHXVQgMajyjfnBotlmyvvApR2iId-4OVQhO9kGPQfJ1"
            embed = {
                "title": "",
                "description": "",
                "color": 16711680, 
                "fields": [
                    {
                        "name": f"<a:cheer1000:1216342513032495144>** | {msg}**",
                        "value": f""
                    }
                ]
            }
            data = {
                "embeds": [embed]
            }
            headers = {
                "Content-Type": "application/json"
            }
            response = requests.post(web, data=json.dumps(data), headers=headers)

            if response.status_code == 200:
                print("webhook sucesso!")
            else:
                print("webhook: ", response.status_code)
        except:
            print("erro webhook")
    elif op == "outros":
        try:
            web = "https://discord.com/api/webhooks/1216332816338391040/V6nY3359cBCjjNN3lKmB1v57z8BDB0UpkVq5yMjK7uH2b14ICLvqynsK8tDSwUpExIC5"
            embed = {
                "title": "",
                "description": "",
                "color": 16711680, 
                "fields": [
                    {
                        "name": f"<a:cheer1000:1216342513032495144>** | {msg}**",
                        "value": f""
                    }
                ]
            }
            data = {
                "embeds": [embed]
            }
            headers = {
                "Content-Type": "application/json"
            }
            response = requests.post(web, data=json.dumps(data), headers=headers)

            if response.status_code == 200:
                print("webhook sucesso!")
            else:
                print("webhook: ", response.status_code)
        except:
            print("erro webhook")        
    elif op == "registar":
        try:
            web = "https://discord.com/api/webhooks/1216346792531066900/nV2SZ9ca5R_g4zGWfC5W5p88mp5iuYlO-6WDb0xVQWZTilEoQzAVgf9Ka0EZAy2EbS3R"
            embed = {
                "title": "",
                "description": "",
                "color": 16711680, 
                "fields": [
                    {
                        "name": f"<a:cheer1000:1216342513032495144>** | {msg}**",
                        "value": f""
                    }
                ]
            }
            data = {
                "embeds": [embed]
            }
            headers = {
                "Content-Type": "application/json"
            }
            response = requests.post(web, data=json.dumps(data), headers=headers)

            if response.status_code == 200:
                print("webhook sucesso!")
            else:
                print("webhook: ", response.status_code)
        except:
            print("erro webhook")
    elif op == "bot":
        try:
            web = "https://discord.com/api/webhooks/1216805075511541860/AZ2dKGk84YHdKUsWVCmBn2RG6WLgNnqx0FueNF6bdN5EYyvzm5TiJJYwnWVRe8v9bePd"
            embed = {
                "title": "",
                "description": "",
                "color": 16711680, 
                "fields": [
                    {
                        "name": f"<a:cheer1000:1216342513032495144>** | {msg}**",
                        "value": f""
                    }
                ]
            }
            data = {
                "embeds": [embed]
            }
            headers = {
                "Content-Type": "application/json"
            }
            response = requests.post(web, data=json.dumps(data), headers=headers)

            if response.status_code == 200:
                print("webhook sucesso!")
            else:
                print("webhook: ", response.status_code)
        except:
            print("erro webhook")
    elif op == "erros":
        try:
            web = "https://discord.com/api/webhooks/1216823221928857630/75MfAxAtNeCvmc-SnIc8r0iK2ePeKxHebjREI5HnZGjJSXGhfJMsDoIXdqYlA0dMLk4_"
            embed = {
                "title": "",
                "description": "",
                "color": 16711680, 
                "fields": [
                    {
                        "name": f"<a:cheer1000:1216342513032495144>** | {msg}**",
                        "value": f""
                    }
                ]
            }
            data = {
                "embeds": [embed]
            }
            headers = {
                "Content-Type": "application/json"
            }
            response = requests.post(web, data=json.dumps(data), headers=headers)

            if response.status_code == 200:
                print("webhook sucesso!")
            else:
                print("webhook: ", response.status_code)
        except:
            print("erro webhook")

try:
    with open('config.json', 'r') as arquivo:
        dados = json.load(arquivo)
except FileNotFoundError:
    dados = {} 

#ligar bot
@bot.event
async def on_ready():
    if dados['logs'] == "True":
        m = f"bot iniciado - PCERJ-REGISTRO 🤖⚡"
        send_web(m, "bot")
    print(f'Bot ligado com sucesso {bot.user}')

#/registrar
@bot.slash_command(name="registrar", description="「❗」Registra-se")
async def registrar(ctx, nome: str, id: int, cargo: str, transferencia: str, autorizacao: disnake.Member):
    if len(nome) > 13:
        await ctx.send(f"**O nome deve ter no máximo 13 caracteres.** <@{ctx.author.id}>", delete_after=10)
        return
     
    if dados['logs'] == "True":
        m = f"Usuario `{ctx.author.display_name}` usou `/registrar`"
        send_web(m, "registar")

    if dados["config"] == "True":
        await ctx.send(f"**Porfavor use: **`/config`** para configurar o bot**", delete_after=10)
    else:
        id_pessoa = ctx.author.id
        autor = ctx.author
        nome_ = nome
        idc_ = id
        embed = disnake.Embed(
            title="PCERJ",
            color=disnake.Color.blurple()
        )
        
        embed.add_field(name="", value=f"**Nome:** `{nome}`\n**Id:** `{id}`\n**Cargo:** `{cargo}`\n**Transferencia:** `{transferencia}`\n**Usuario:** <@{id_pessoa}>\n**Autorizacao:** {autorizacao.mention}", inline=False)
        
        if ctx.author.avatar:
            embed.set_thumbnail(url=ctx.author.avatar.url)

        canal_destino = bot.get_channel(dados["id-logs"])
        await ctx.send(f"Pronto!, Só aguardar.. {autor.mention}", delete_after=5)
        buttons = [
            disnake.ui.Button(style=disnake.ButtonStyle.gray, label="[👮‍♂️ REC]", custom_id=f"a_{id_pessoa}_{nome_}_{idc_}"),
            disnake.ui.Button(style=disnake.ButtonStyle.gray, label="[👮‍♂️ AGT-3°]", custom_id=f"b_{id_pessoa}_{nome_}_{idc_}"),
            disnake.ui.Button(style=disnake.ButtonStyle.gray, label="[👮‍♂️ AGT-2°]", custom_id=f"c_{id_pessoa}_{nome_}_{idc_}"),
            disnake.ui.Button(style=disnake.ButtonStyle.gray, label="[👮‍♂️ AGT-1°]", custom_id=f"d_{id_pessoa}_{nome_}_{idc_}"),
            disnake.ui.Button(style=disnake.ButtonStyle.gray, label="[👮‍♂️ AGT-ESP]", custom_id=f"e_{id_pessoa}_{nome_}_{idc_}"),
        ]
        
        view = disnake.ui.View()
        for button in buttons:
            view.add_item(button)

        await canal_destino.send(
            content="Por favor, verifique os dados abaixo ",
            embed=embed,
            view=view
        )


#/ping
@bot.slash_command(name="ping", description="「🏓」Veja o ping do bot.")
async def ping(ctx):
    latency = round(bot.latency * 1000) 
    if latency < 100:
        mensagem = "**⚡| Ping ótimo! O bot está voando!**"
    elif latency < 200:
        mensagem = "**⚡| Ping bom! O bot está ágil.**"
    elif latency < 300:
        mensagem = "**⚡| Ping razoável. O bot está se esforçando.**"
    else:
        mensagem = "**⚡| Ping alto! O bot está um pouco lento.**"

    await ctx.send(f"**🏓| Pong! Ping:** `{latency}ms`\n{mensagem}")


#/reset
@bot.slash_command(name="reset", description="「⚠️」Resetar Config")
async def reset(ctx):
    if not ctx.author.guild_permissions.administrator: 
        await ctx.send("Você não tem permissão para usar este comando.")
        if dados['logs'] == "True":
            m = f"Usuario `{ctx.author.display_name}` usou `/reset` sem permissão ⚠️"
            send_web(m, "outros")
        return
    

    dados["id-logs"] = 0
    dados["id-rec"] = 0
    dados["id-serve"] = 0
    dados["id-agt3"] = 0
    dados["id-agt2"] = 0
    dados["id-agt1"] = 0
    dados["id-agtesp"] = 0
    dados["id-pcvidigal"] = 0
    dados["id-1bpc"] = 0
    dados["config"] = "True"

    with open('config.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

    if dados['logs'] == "True":
        m = f"Usuario `{ctx.author.display_name}` usou `/reset`"
        send_web(m, "outros")

    await ctx.send(f"**Config resetadas**", delete_after=5)


#/config
@bot.slash_command(name="config", description="「⚙️」Configura o bot.")
async def config(ctx, canal_de_logs: disnake.TextChannel, serve_id: str, cargo_recruta: disnake.Role, cargo_agt3: disnake.Role, cargo_agt2: disnake.Role, cargo_agt1: disnake.Role, cargo_agt_esp: disnake.Role, cargo_pcvifigal: disnake.Role, cargo_1bpc: disnake.Role):
    if not ctx.author.guild_permissions.administrator: 
        await ctx.send("Você não tem permissão para usar este comando.")
        if dados['logs'] == "True":
            m = f"Usuario `{ctx.author.display_name}` usou `/config` sem permissão ⚠️"
            send_web(m, "outros")
        return
    
    await ctx.send(f'# Configurações:\n'
                   f'Canal de Logs: {canal_de_logs.mention}\n'
                   f'Recruta: {cargo_recruta.mention}\n'
                   f'AGT 3: {cargo_agt3.mention}\n'
                   f'AGT 2: {cargo_agt2.mention}\n'
                   f'AGT 1: {cargo_agt1.mention}\n'
                   f'AGT ESP: {cargo_agt_esp.mention}\n'
                   f'PC VIDIGAL: {cargo_pcvifigal.mention}\n'
                   f'1BPC: {cargo_1bpc.mention}')


    
    id_logs = canal_de_logs.id
    rec = cargo_recruta.id
    agt3 = cargo_agt3.id
    agt2 = cargo_agt2.id
    agt1 = cargo_agt1.id
    agtESP = cargo_agt_esp.id
    pcvidigal = cargo_pcvifigal.id
    PriBPC = cargo_1bpc.id
    guld = int(serve_id)
    dados["id-logs"] = id_logs
    dados["id-rec"] = rec
    dados["id-serve"] = guld
    dados["id-agt3"] = agt3
    dados["id-agt2"] = agt2
    dados["id-agt1"] = agt1
    dados["id-agtesp"] = agtESP
    dados["id-pcvidigal"] = pcvidigal
    dados["id-1bpc"] = PriBPC
    dados["config"] = "False"

    with open('config.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

    if dados['logs'] == "True":
        m = f"Usuario `{ctx.author.display_name}` usou `/config`"
        send_web(m, "outros")


#/clear
@bot.slash_command(name="clear", description="「🗑️」Limpar Chat")
async def clear(ctx, amount: int):
    if not ctx.author.guild_permissions.administrator: 
        await ctx.send("Você não tem permissão para usar este comando.")
        if dados['logs'] == "True":
            m = f"Usuario `{ctx.author.display_name}` tenteu usar `/clear` sem permissão ⚠️"
            send_web(m, "outros")
        return
    
    await ctx.channel.purge(limit=amount + 1)
    print(f"Chat limpo por {ctx.author}")
    await ctx.send(f"Chat limpo por <@{ctx.author.id}>")
    if dados['logs'] == "True":
        m = f"Usuario `{ctx.author.display_name}` usou `/clear`"
        send_web(m, "outros")

@bot.slash_command(name="logs", description="「⚙️」logs-pcerj")
async def logs(ctx):
    d = dados['logs']
    
    if d == "True":
        dados["logs"] = "False"
        with open('config.json', 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
        await ctx.send("**LOGS OFF**", delete_after=5)
    else:
        dados["logs"] = "True"
        with open('config.json', 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
        await ctx.send("**LOGS ON**", delete_after=5)

#opcao buttons
@bot.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
    button_id, id_pessoa, nome_, idc_ = inter.component.custom_id.split("_")
    guild_id = dados["id-serve"]  
    guild = bot.get_guild(guild_id)
    member = await guild.fetch_member(int(id_pessoa))  
    n_nick = f"[REC] {nome_} | {idc_}"
    n1_nick = f"[AGT-3°] {nome_} | {idc_}"
    n2_nick = f"[AGT-2°] {nome_} | {idc_}"
    n3_nick = f"[AGT-1°] {nome_} | {idc_}"
    n4_nick = f"[AGT-ESP] {nome_} | {idc_}"
    pc_vidigal = member.guild.get_role(int(dados['id-pcvidigal']))
    PrimeiroBPC = member.guild.get_role(int(dados['id-1bpc']))
    Recruta = member.guild.get_role(int(dados['id-rec']))
    agt3 = member.guild.get_role(int(dados['id-agt3']))
    agt2 = member.guild.get_role(int(dados['id-agt2']))
    agt1 = member.guild.get_role(int(dados['id-agt1']))
    agtesp = member.guild.get_role(int(dados['id-agtesp']))
    print("tes")

    if button_id not in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        return

    if button_id == "a":
        print(pc_vidigal, PrimeiroBPC, Recruta, agt3, agt2, agt1, agtesp)
        await inter.response.send_message(f"Setado!!", delete_after=2)
        await member.edit(nick=n_nick)  
        print(f"Apelido alterado para {n_nick}!") 
        await member.remove_roles(pc_vidigal, PrimeiroBPC, Recruta, agt3, agt2, agt1, agtesp)
        await member.add_roles(pc_vidigal, PrimeiroBPC, Recruta)
        print(f"O cargo com ID {Recruta} foi adicionado a {n_nick}.")
        if dados['logs'] == "True":
            m = f"Usuario `{inter.author.display_name}` setou `{n_nick}`"
            send_web(m, "set")





    elif button_id == "b":
        await inter.response.send_message(f"Setado!!", delete_after=2)
        try:
            await member.edit(nick=n1_nick)  
            print(f"Apelido alterado para {n1_nick}!")
            
            try:
                await member.remove_roles(pc_vidigal, PrimeiroBPC, Recruta, agt3, agt2, agt1, agtesp)
                await member.add_roles(pc_vidigal, PrimeiroBPC, agt3)
                print(f"O cargo com ID {agt3} foi adicionado a {n1_nick}.")
                if dados['logs'] == "True":
                    m = f"Usuario `{inter.author.display_name}` setou `{n1_nick}`"
                    send_web(m, "set")
                
            except disnake.errors.Forbidden:
                if dados['logs'] == "True":
                    m = "⚠️BOT SEM PERMISSAO⚠️ (erro ao colocar cargos)"
                    send_web(m, "erros")

                print("⚠️BOT SEM PERMISSAO⚠️ (erro ao colocar cargos)")
                
            except Exception as e:
                if dados['logs'] == "True":
                    m = "⚠️BOT SEM PERMISSAO⚠️ (erro ao adicionar cargos)"
                    send_web(m, "erros")

                print(f"⚠️BOT SEM PERMISSAO⚠️ (erro ao adicionar cargos)")

        except disnake.errors.Forbidden:
            if dados['logs'] == "True":
                m = "⚠️BOT SEM PERMISSAO⚠️ (erro ao mudar nome)"
                send_web(m, "erros")
            print("⚠️BOT SEM PERMISSAO⚠️ (erro ao mudar nome)")

        except disnake.errors.NotFound:
            if dados['logs'] == "True":
                m = "⚠️User nao existe⚠️"
                send_web(m, "erros")
                
            print("⚠️User nao existe⚠️")




    elif button_id == "c":
        await inter.response.send_message(f"Setado!!", delete_after=2)
        try:
            await member.edit(nick=n2_nick)  
            print(f"Apelido alterado para {n2_nick}!")
            
            try:
                await member.remove_roles(pc_vidigal, PrimeiroBPC, Recruta, agt3, agt2, agt1, agtesp)
                await member.add_roles(pc_vidigal, PrimeiroBPC, agt2)
                print(f"O cargo com ID {agt2} foi adicionado a {n2_nick}.")
                if dados['logs'] == "True":
                    m = f"Usuario `{inter.author.display_name}` setou `{n2_nick}`"
                    send_web(m, "set")
                
            except disnake.errors.Forbidden:
                if dados['logs'] == "True":
                    m = "⚠️BOT SEM PERMISSAO⚠️ (erro ao colocar cargos)"
                    send_web(m, "erros")

                print("⚠️BOT SEM PERMISSAO⚠️ (erro ao colocar cargos)")
                
            except Exception as e:
                if dados['logs'] == "True":
                    m = "⚠️BOT SEM PERMISSAO⚠️ (erro ao adicionar cargos)"
                    send_web(m, "erros")

                print(f"⚠️BOT SEM PERMISSAO⚠️ (erro ao adicionar cargos)")

        except disnake.errors.Forbidden:
            if dados['logs'] == "True":
                m = "⚠️BOT SEM PERMISSAO⚠️ (erro ao mudar nome)"
                send_web(m, "erros")
            print("⚠️BOT SEM PERMISSAO⚠️ (erro ao mudar nome)")

        except disnake.errors.NotFound:
            if dados['logs'] == "True":
                m = "⚠️User nao existe⚠️"
                send_web(m, "erros")
                
            print("⚠️User nao existe⚠️")


    elif button_id == "d":
        await inter.response.send_message(f"Setado!!", delete_after=2)
        try:
            await member.edit(nick=n3_nick)  
            print(f"Apelido alterado para {n3_nick}!")
            
            try:
                await member.remove_roles(pc_vidigal, PrimeiroBPC, Recruta, agt3, agt2, agt1, agtesp)
                await member.add_roles(pc_vidigal, PrimeiroBPC, agt1)
                print(f"O cargo com ID {agt1} foi adicionado a {n3_nick}.")
                if dados['logs'] == "True":
                    m = f"Usuario `{inter.author.display_name}` setou `{n3_nick}`"
                    send_web(m, "set")
                
            except disnake.errors.Forbidden:
                if dados['logs'] == "True":
                    m = "⚠️BOT SEM PERMISSAO⚠️ (erro ao colocar cargos)"
                    send_web(m, "erros")

                print("⚠️BOT SEM PERMISSAO⚠️ (erro ao colocar cargos)")
                
            except Exception as e:
                if dados['logs'] == "True":
                    m = "⚠️BOT SEM PERMISSAO⚠️ (erro ao adicionar cargos)"
                    send_web(m, "erros")

                print(f"⚠️BOT SEM PERMISSAO⚠️ (erro ao adicionar cargos)")

        except disnake.errors.Forbidden:
            if dados['logs'] == "True":
                m = "⚠️BOT SEM PERMISSAO⚠️ (erro ao mudar nome)"
                send_web(m, "erros")
            print("⚠️BOT SEM PERMISSAO⚠️ (erro ao mudar nome)")

        except disnake.errors.NotFound:
            if dados['logs'] == "True":
                m = "⚠️User nao existe⚠️"
                send_web(m, "erros")
                
            print("⚠️User nao existe⚠️")



    elif button_id == "e":
        await inter.response.send_message(f"Setado!!", delete_after=2)
        try:
            await member.edit(nick=n4_nick)  
            print(f"Apelido alterado para {n4_nick}!")
            
            try:
                await member.remove_roles(pc_vidigal, PrimeiroBPC, Recruta, agt3, agt2, agt1, agtesp)
                await member.add_roles(pc_vidigal, PrimeiroBPC, agtesp)
                print(f"O cargo com ID {agtesp} foi adicionado a {n4_nick}.")
                if dados['logs'] == "True":
                    m = f"Usuario `{inter.author.display_name}` setou `{n4_nick}`"
                    send_web(m, "set")
                
            except disnake.errors.Forbidden:
                if dados['logs'] == "True":
                    m = "⚠️BOT SEM PERMISSAO⚠️ (erro ao colocar cargos)"
                    send_web(m, "erros")

                print("⚠️BOT SEM PERMISSAO⚠️ (erro ao colocar cargos)")
                
            except Exception as e:
                if dados['logs'] == "True":
                    m = "⚠️BOT SEM PERMISSAO⚠️ (erro ao adicionar cargos)"
                    send_web(m, "erros")

                print(f"⚠️BOT SEM PERMISSAO⚠️ (erro ao adicionar cargos)")

        except disnake.errors.Forbidden:
            if dados['logs'] == "True":
                m = "⚠️BOT SEM PERMISSAO⚠️ (erro ao mudar nome)"
                send_web(m, "erros")
            print("⚠️BOT SEM PERMISSAO⚠️ (erro ao mudar nome)")

        except disnake.errors.NotFound:
            if dados['logs'] == "True":
                m = "⚠️User nao existe⚠️"
                send_web(m, "erros")
                
            print("⚠️User nao existe⚠️")


bot.run(dados["token"])
