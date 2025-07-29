# Trivia by API-Ninjas MCP Server

Welcome to the **Trivia by API-Ninjas** MCP Server! This server is designed to provide you with endless trivia questions and answers across a wide range of fascinating topics. Whether you're a trivia enthusiast or just looking to expand your knowledge, this server will deliver random trivia that is both entertaining and educational.

## Features

- **Extensive Database**: Access a vast collection of trivia questions and answers covering topics such as science, literature, philosophy, and more.
- **Randomized Trivia**: Get random trivia questions each time, ensuring a fresh and engaging experience.
- **Customizable Queries**: Tailor the trivia experience according to your preferences using various parameters.

## Tool List

The MCP server utilizes the following tool to deliver its trivia content:

- **Trivia Tool**: 
  - **Endpoint**: `/v1/trivia`
  - **Description**: This tool fetches random trivia questions and answers.
  - **Parameters**:
    - **Category**: (Optional) Specify the category of trivia questions you are interested in. Possible values include:
      - `artliterature`
      - `language`
      - `sciencenature`
      - `general`
      - `fooddrink`
      - `peopleplaces`
      - `geography`
      - `historyholidays`
      - `entertainment`
      - `toysgames`
      - `music`
      - `mathematics`
      - `religionmythology`
      - `sportsleisure`
    - **Limit**: (Optional) Define the number of trivia results you want to receive. The limit must be between 1 and 30, with a default value of 1.

## Usage

To make the most out of the Trivia by API-Ninjas MCP Server, you can customize your queries by selecting a specific category and setting the desired number of trivia questions. This flexibility allows you to create a tailored trivia experience that suits your interests and needs.

Explore the endless possibilities with the Trivia by API-Ninjas MCP Server and enjoy a seamless trivia experience that is both fun and informative!