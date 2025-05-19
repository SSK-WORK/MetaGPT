from metagpt.team import Team
from metagpt.roles import Architect, ProjectManager, ProductManager, Engineer, QaEngineer

async def main():
    team = Team()
    team.hire([
        ProductManager(),
        Architect(),
        ProjectManager(),
        Engineer(n_working_threads=3),
        QaEngineer(),
    ])
    prompt = "Develop a mobile application for ordering food from local restaurants, including user authentication, menu browsing, order placement, and payment integration. Also, prepare a sales strategy for its launch."
    result = await team.run(prompt=prompt)
    print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())