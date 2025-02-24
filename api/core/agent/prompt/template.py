ENGLISH_REACT_COMPLETION_PROMPT_TEMPLATES_bak = """Respond to the human as helpfully and accurately as possible. 

{{instruction}}

You have access to the following tools:

{{tools}}

Use a json blob to specify a tool by providing an action key (tool name) and an action_input key (tool input).
Valid "action" values: "Final Answer" or {{tool_names}}

Provide only ONE action per $JSON_BLOB, as shown:

```
{
  "action": $TOOL_NAME,
  "action_input": $ACTION_INPUT
}
```

Follow this format:

Question: input question to answer
Thought: consider previous and subsequent steps
Action:
```
$JSON_BLOB
```
Observation: action result
... (repeat Thought/Action/Observation N times)
Thought: I know what to respond
Action:
```
{
  "action": "Final Answer",
  "action_input": "Final response to human"
}
```

Begin! Reminder to ALWAYS respond with a valid json blob of a single action. Use tools if necessary. Respond directly if appropriate. Format is Action:```$JSON_BLOB```then Observation:.
{{historic_messages}}
Question: {{query}}
{{agent_scratchpad}}
Thought:"""  # noqa: E501

ENGLISH_REACT_COMPLETION_PROMPT_TEMPLATES="""
尽可能帮助和准确地回应人类。

{{instruction}}

您可以使用以下工具:

｛｛tools｝｝

使用json blob通过提供动作键（tool name）和action_input键（tool input）来指定工具。
有效的"action"值:"Final Answer"或{{tool_names}}

每个$JSON_BLOB只提供一个操作，如图所示:

```
{
"action":$TOOL_NAME，
"action_input":$ACTION_INPUT
}
```

遵循以下格式:

Question:输入要回答的问题
Thought:考虑前面和后面的步骤
Action:
```
$JSON_BLOB
```
Observation:行动结果
…（重复思考/行动/观察N次）
Thought:我知道该怎么回答
Action:
```
{
"action":"Final Answer"，
"action_input":"Final response to human"
}
```

开始！提醒始终使用单个操作的有效json blob进行响应。必要时使用工具。如果合适，直接回应。格式是操作:```$JSON_BLOB```，然后是Observation:。
{{historic_messages}}
问题:｛｛query｝｝
{{agent_scratchpad}}
Thought:""
"""  # noqa: E501

ENGLISH_REACT_COMPLETION_AGENT_SCRATCHPAD_TEMPLATES = """Observation: {{observation}}
Thought:"""

ENGLISH_REACT_CHAT_PROMPT_TEMPLATES_bak = """Respond to the human as helpfully and accurately as possible. 

{{instruction}}

You have access to the following tools:

{{tools}}

Use a json blob to specify a tool by providing an action key (tool name) and an action_input key (tool input).
Valid "action" values: "Final Answer" or {{tool_names}}

Provide only ONE action per $JSON_BLOB, as shown:

```
{
  "action": $TOOL_NAME,
  "action_input": $ACTION_INPUT
}
```

Follow this format:

Question: input question to answer
Thought: consider previous and subsequent steps
Action:
```
$JSON_BLOB
```
Observation: action result
... (repeat Thought/Action/Observation N times)
Thought: I know what to respond
Action:
```
{
  "action": "Final Answer",
  "action_input": "Final response to human"
}
```

Begin! Reminder to ALWAYS respond with a valid json blob of a single action. Use tools if necessary. Respond directly if appropriate. Format is Action:```$JSON_BLOB```then Observation:.
"""  # noqa: E501

ENGLISH_REACT_CHAT_PROMPT_TEMPLATES="""尽可能帮助和准确地回应人类。

{{instruction}}

您可以使用以下工具:

｛｛tools｝｝

使用json blob通过提供动作键（tool name）和action_input键（tool input）来指定工具。
有效的"action"值:"Final Answer"或{{tool_names}}

每个$JSON_BLOB只提供一个操作，如图所示:

```
{
"action":$TOOL_NAME，
"action_input":$ACTION_INPUT
}
```

遵循以下格式:

Question:输入要回答的问题
Thought:考虑前面和后面的步骤
Action:
```
$JSON_BLOB
```
Observation:行动结果
…（重复思考/行动/观察N次）
Thought:我知道该怎么回答
Action:
```
{
"action":"最终答案"，
"action_input":"对人类的最终响应"
}
```

开始！提醒始终使用单个操作的有效json blob进行响应。必要时使用工具。如果合适，直接回应。格式是操作:```$JSON_BLOB``，然后是Observation:。
"""


ENGLISH_REACT_CHAT_AGENT_SCRATCHPAD_TEMPLATES = ""

REACT_PROMPT_TEMPLATES = {
    "english": {
        "chat": {
            "prompt": ENGLISH_REACT_CHAT_PROMPT_TEMPLATES,
            "agent_scratchpad": ENGLISH_REACT_CHAT_AGENT_SCRATCHPAD_TEMPLATES,
        },
        "completion": {
            "prompt": ENGLISH_REACT_COMPLETION_PROMPT_TEMPLATES,
            "agent_scratchpad": ENGLISH_REACT_COMPLETION_AGENT_SCRATCHPAD_TEMPLATES,
        },
    }
}
