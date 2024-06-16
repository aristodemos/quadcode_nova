from h2o_wave import main, app, Q, ui, data
import ollama
from chroma_textdb import get_relevant_docs

# stream = ollama.chat(
#     model='llama3',
#     messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
#     stream=True,
# )
#
# for chunk in stream:
#   print(chunk['message']['content'], end='', flush=True)

@app('/chatbot')
async def serve(q: Q):
    if not q.client.initialized:
        # Use list buffer to allow easy streaming. Must have exactly 2 fields - content and from_user.
        q.page['example'] = ui.chatbot_card(box='1 1 5 5', data=data(fields='content from_user', t='list'), name='chatbot')
        q.client.initialized = True

    # A new message arrived.
    if q.args.chatbot:
        # Append user message.
        q.page['example'].data += [q.args.chatbot, True]
        # Append bot response.
        q.page['example'].data += ['', False]

        modify_question = q.args.chatbot
        if len(modify_question.split()) <= 10:
            relevant_txt = get_relevant_docs(modify_question, 1)
            if len(relevant_txt) < 1:
                pass
            else:
                modify_question = f'{modify_question} Answer this question. You can use this text to enrich your references: '
                for t in relevant_txt:
                    modify_question += f' {t}'

        stream = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': modify_question}],
            stream=True,
        )
        reply = ''
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
            await q.sleep(0.1)
            reply += chunk['message']['content'] + ''
            q.page['example'].data[-1] = [reply, False]
            await q.page.save()

        # Stream bot response.
        # stream = ''
        # for w in 'I am a fake chatbot. Sorry, I cannot help you.'.split():
        #     await q.sleep(0.1)
        #     stream += w + ' '
        #     q.page['example'].data[-1] = [stream, False]
        #     await q.page.save()

    await q.page.save()