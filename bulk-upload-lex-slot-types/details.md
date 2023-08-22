<h3>Overview:</h3>
<p>Lex V2 is an AWS service which allows users to build conversational bot for applications using voice and text. An Amazon Lex V2 bot has certain structure containing intents, slots, slot-types, aliases, locale, utterances, prompts, etc. which confer to the bot creation.</p>
<p>Bot intents can be understood as goals that the user wants to achieve, such as, “ordering a flower” or “ordering a pizza”. There should always be at-least one intent per bot.
Each intent has an optional slot in it.</p>
<p>Slots are parameters that are required for fulfilling an intent. These parameters receive its value from end- users by generating a prompt, which are basically questions asked to the client and the inputs provided are stored as its value.
Each slot has a type that defines the values that can be entered in the slot.</p>
<p>“Slot-types” can be either built-in such as AMAZON.City, AMAZON.Country, AMAZON.Date, or custom slot- type.</p>
For a custom slot-type, you can provide a list of values that Lex V2 uses to train the machine learning model to recognise values for a slot.
<p>For example: you can define slot-type as “Genres” with values as “comedy”, “adventure”, “documentary”, etc.
Users can also define synonyms for each of the values, such as, synonym for “comedy” can be “funny” and “humorous”.</p>
The slot-type resolution can be configured to one of the following:
<ol>
<li> expand the slot values: slot values will be used as training data and the model will resolve the slot to the value provided by the user, if it is similar to the slot values present.</li>
<li>restrict resolution to slot values: there will be additional possible values that can be added for each resolved slot-value. Each entry by the client will be stored as the resolved slot-value.</li>
</ol>
<p>These values can either be filled through AWS Lex console or through API calls. For each slot-type, users can have a maximum of 10,000 values and synonyms. Each bot can have 50,000 slot-type values and synonyms.</p>
<h3>Problem Statement:</h3>
<p>There are scenarios where users have large set of slot-type values which they need to add to the bot.</p>
<p>However at present, AWS Lex console lacks the feature that allows user to perform bulk ingestion of such data.
<b>Currently, these training data needs to be added one at a time in the console, example, if there are 1000 or more number of slot-type values that needs to be added in the bot.</b></p>
Alternatively, you can utilise Lex API calls for the same, but, it will involve creating scripts from scratch, but using cloudformation, this has been automated.
<h3>Working:</h3>
<p>CloudFormation will create an S3 bucket and a Lambda function with pre-defined code script and IAM permissions. The S3 bucket created will have event notifications set in-order to trigger the Lambda function for bucket-level operation.</p>
<p>The S3 operation that will create a notification is object creation or upload. So, when the end-user will upload a CSV file containing thousands of Lex V2 slot-type values in it, an event notification generated will in-turn trigger Lambda function.</p>
<p>This lambda function will contain valid scripts that will read the CSV file from S3 bucket and make an “update slot type” API call to target Lex V2 bot.
Based on this, each line in CSV file will be read and uploaded in the bot slot-type.</p>
<b>Please refer the workflow diagram for better understanding.</b>
