# Planning

## Models

#### Member
Login info, profile

#### Artist
Analogue to company in github. Has multiple members and a collection of songs.

#### Song
Analogue to repo in github. Owned by an artist.

#### Revision
Analogue to a commit in github. Represents a change to a song.

#### Draft
Analogue to a branch in github. Represents a separate version of a song.

#### Suggestion
Analogue to a pull request in github. Represents a new draft to a song to be reviewed/discussed by other members in the band.

#### Role
Permissions for member in the context of an Artist, e.g. founding member, key member, contributing member (also maybe fan (read-only))

#### Rules
Rules for how content is created, approved, seen, etc. Can be tied to Artists or Songs.


## Workflow

Create a new song ->
Create first draft, designated as Master ->
Can make revisions on master draft (if song rules allow) ->
Alternatively, make new drafts of the song, make revisions there, and then make a suggestion to change the master draft (according to the branch)