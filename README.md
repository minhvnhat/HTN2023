# HTN2023

### Backend for our HTN 2023 project, BudEJournal!

### Project brief:
Our app is a journalling app that has the user enter 2 journal entries a day. One in the morning and one in the evening. During these journal entries, it would ask the user about their mood at the moment, generate am appropriate response based on their mood, and then ask questions that get the user to think about such as gratuity, their plans for the day, and what advice would they give themselves. Our questions follow many of the common journalling practices. The second journal entry then follows a similar format of mood and questions with a different set of questions to finish off the user's day. These help them reflect and look forward to the upcoming future. Our most powerful feature would be the AI that takes data such as emotions and keywords from answers and helps users generate journal summaries across weeks, months, and years. These summaries would then provide actionable steps the user could take to make self-improvements.

### Functionalities:
- REST API that can receive Journal (and Mood) entires and share it.
- Integration with Large Language Model to summarize journal entries cross weeks, months, and years.

### Tech used:
- [Python Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [CockroachDB](https://www.cockroachlabs.com/) with [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
- [Cohere's Co.Chat API](https://docs.cohere.com/reference/post_chat)

### Other links:
- [Figma](https://www.figma.com/proto/5hnPokrci4UtlAkOJWrS6f/budEjournal?page-id=0%3A1&type=d[…]rting-point-node-id=29%3A1906&show-proto-sidebar=1&mode=design)
- [Front-end](https://github.com/BaileyLuu/budejournal/tree/main)
- [Devpost](https://devpost.com/software/budejournal)
