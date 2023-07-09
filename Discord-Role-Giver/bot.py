import csv
import discord

async def assign_roles(csv_file, guild):
    # Get the Member role
    member_role = None
    for role in guild.roles:
        if role.name == "Member":
            member_role = role
            break

    if not member_role:
        print("Error: Member role not found")
        return

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if present

        for row in reader:
            name = row[0]
            role_name = row[1]
            role = discord.utils.get(guild.roles, name=role_name)

            member = guild.get_member_named(name)
            if not member:
                print(f"Error: Member {name} not found in server")
                continue

            # Add specified role in addition to Member role if specified in CSV
            if role:
                await member.add_roles(role)
                print(f"Assigned role {role.name} to {member.name}")
            await member.add_roles(member_role)
            print(f"Assigned role {member_role.name} to {member.name}")

async def on_message(message):
    if message.content.startswith('!assign_roles'):
        await assign_roles('roles.csv', message.guild)
        await message.channel.send('Roles assigned successfully!')

# Example usage
client.run('your_token_here')
