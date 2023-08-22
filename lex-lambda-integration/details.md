Lex V2 service helps building conversational bots with dynamic responses. However, we can utilise a Lambda function to our advantage in-order to get more flexibility in the way bot interacts with a user.

A lambda function follows a certain JSON format to send responses to a Lex V2 bot. Similarly, Lex V2 bot send responses in a certain JSON format, back to Lambda. Please follow documentation to observe the said format.

Cloud-formation will remove the hassle of setting up a Lex V2 bot and Lambda function. Moreover, the bot will be readily available to interact with Lambda function, with a pre-defined script, describing the proper JSON format required for interaction.

<b>Steps to be followed:</b>

    1. Create a stack using cloud-formation template "OrderPizzaBot.yaml".

    2. Once the stack creation is complete, a Lex V2 bot "OrderPizzaWithCFN" and a Lambda function "OrderMyPizzaFunc", with Python 3.9 runtime will be available.

    3. Visit "OrderPizzaWithCFN" bot and build the bot. 

    4. Your bot will be ready for testing.

    5. enter "order pizza" to trigger "DesignYourPizza" intent.

<b>NOTE:</b>

    1. the bot will be created with default "DRAFT" version and "TestBotAlias", which is only meant for testing.

    2. intent switching has been demonstrated by eliciting slots of another intent. There can be different ways to do that, for example, eliciting an intent to trigger it or delegating the current intent.

    3. custom slots has been demonstrated with "default" slot type resolution. 

    4. slot elicitation with working Lex V2 bot and Lambda exchange of responses has been implemented.

    5. intent confirmation along with fulfilment has been added.
