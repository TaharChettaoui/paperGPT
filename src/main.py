import os
import openai
import wget
import pathlib
import pdfplumber
import numpy as np


def get_paper(paper_url, filename="random_paper.pdf"):
    """ Download the paper from it's arxiv page and returns the local path to that file."""
    downloadedPaper = wget.download(paper_url, filename)    
    downloadedPaperFilePath = pathlib.Path(downloadedPaper)

    return downloadedPaperFilePath

def display_paper_content(paper_content, page_start=0, page_end=1):
    """Display the paper content. """
    for page in paper_content[page_start:page_end]:
        print(page.extract_text())


def show_paper_summary(paperContent, openai_organization, openai_api_key, file_name="output.txt"):
    """ Feed the text to the GPT-3 model using the openai api. """
    # Tag for the model to inform about text start and end
    tldr_tag = "\n tl;dr:"

    # Model set up
    openai.organization = openai_organization
    openai.api_key = openai_api_key
    engine_list = openai.Engine.list() 
    
    # Summarize each page
    with open(file_name, 'w', encoding="utf-8") as f:
        for page in paperContent:    
            text = page.extract_text() + tldr_tag

            # feeding the text to the model
            response = openai.Completion.create(engine="text-davinci-003",prompt=text,temperature=0.3,
                max_tokens=500,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.3,
                stop=["\n"]
            )

            f.write(response["choices"][0]["text"] + "\n")


if __name__ == "__main__":
    filename = "ppo.pdf"
    paper_url = "https://arxiv.org/pdf/1707.06347.pdf"
    # https://platform.openai.com/account/org-settings
    openai_organization = "TODO"
    # https://platform.openai.com/account/api-keys
    openai_api_key = "TODO"

    # Check if file already exists
    if not os.path.exists(filename):
        get_paper(paper_url, filename)

    paper_content = pdfplumber.open(filename).pages
    # display_paper_content(paper_content)

    show_paper_summary(paper_content, openai_organization, openai_api_key)