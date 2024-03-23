:::mermaid
flowchart LR
    userInput["`**User Input**`"]
    promptTemplate["`**Prompt Template**`"]
    chatModel["`**Chat Model**`"]
    strOutputParser["`**String Output Parser**`"]
    result["`**Result**`"]
    userInput-->|Dict|promptTemplate
    promptTemplate -->|PromptValue|chatModel
    chatModel -->|ChatMessage|strOutputParser
    strOutputParser -->|String|result
:::