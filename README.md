# Startuplane API

**version**: *1.0.0*

## candidate

candidate

### This API create candidate

Candidate create API takes firstname, lastname, email that is required to create candidate.About field takes details of candidate career plan takes candidtate carrer objects

**route:** `/api/candidate/candidate/`

**method:** `POST`

**requestBody:** 

*application/json*

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| firstname | string | True |  |
| lastname | string | True |  |
| email | string | True |  |
| about | - | - | [About.__pydantic_model__](#About.__pydantic_model__) |
| careerplan | - | - | [CareerPlan.__pydantic_model__](#CareerPlan.__pydantic_model__) |
| finalbits | - | - | [FinalBits.__pydantic_model__](#FinalBits.__pydantic_model__) |
| id | string | False |  |



### This API get candidate

Candidate get API featch all candidate detail with all feilds

**route:** `/api/candidate/candidate/getall/`

**method:** `GET`



### This API get particular candidate

Candidate get by ID required candidate Id for getting the detail of particular candidate

**route:** `/api/candidate/candidate/get/{id}/`

**method:** `GET`

**parameters:** 

| name | type | in   | required | description |
| ---- | ---- | ---- | -------- | ----------- |
| id | string | path | True |  |



### This API update the data about candidate

Candidate put takes ID of candidate and update the field of candidate data

**route:** `/api/candidate/candidate/update/{id}/`

**method:** `PUT`

**parameters:** 

| name | type | in   | required | description |
| ---- | ---- | ---- | -------- | ----------- |
| id | string | path | True |  |



### This API delete candidate

Candidate delete take id for delete particular candidate

**route:** `/api/candidate/candidate/delete/{objectid}/`

**method:** `DELETE`

**parameters:** 

| name | type | in   | required | description |
| ---- | ---- | ---- | -------- | ----------- |
| id | string | path | True |  |



### This API delete multiple candidate

Candidate bulk delete use for deleting multiple Candidate

**route:** `/api/candidate/candidate/bulk/{objectid}`

**method:** `DELETE`

**parameters:** 

| name | type | in   | required | description |
| ---- | ---- | ---- | -------- | ----------- |
| id | string | path | True |  |



### candidate_bulk_create

Candidate bulk update provide a functionality to create multiple candidate field in one way

**route:** `/api/candidate/candidate/bulk/`

**method:** `POST`

**requestBody:** 

*application/json*

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| firstname | string | True |  |
| lastname | string | True |  |
| email | string | True |  |
| about | - | - | [About.__pydantic_model__](#About.__pydantic_model__) |
| careerplan | - | - | [CareerPlan.__pydantic_model__](#CareerPlan.__pydantic_model__) |
| finalbits | - | - | [FinalBits.__pydantic_model__](#FinalBits.__pydantic_model__) |
| id | string | False |  |




## user

user

### This API create User

User create API takes firstname, lastname, email, password that is required to create user. Role field assigned role of user

**route:** `/api/user/`

**method:** `POST`

**requestBody:** 

*application/json*

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| firstname | string | True |  |
| lastname | string | True |  |
| email | string | True |  |
| password | string | True |  |
| role | string | False |  |
| id | string | False |  |



### This API get all User

User get all provide all user and detail about User

**route:** `/api/user/getall/`

**method:** `GET`



### This API get User by ID

User get takes user id and give a detail about of user

**route:** `/api/user/get/{id}/`

**method:** `GET`

**parameters:** 

| name | type | in   | required | description |
| ---- | ---- | ---- | -------- | ----------- |
| id | string | path | True |  |



### This API update User

User update takes User ID to update the connected ID user

**route:** `/api/user/update/{id}/`

**method:** `PUT`

**parameters:** 

| name | type | in   | required | description |
| ---- | ---- | ---- | -------- | ----------- |
| id | string | path | True |  |



### This API delete user

User delete takes ID of user which wants to delete

**route:** `/api/user/delete/{id}/`

**method:** `DELETE`

**parameters:** 

| name | type | in   | required | description |
| ---- | ---- | ---- | -------- | ----------- |
| id | string | path | True |  |



### This API login user

User login provide a token and refresh token for using any API permission of

**route:** `/api/user/login/`

**method:** `POST`

**requestBody:** 

*application/json*

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| email | string | True |  |
| password | string | True |  |



### This API logout user

User logout provide us facility to blacklist the token

**route:** `/api/user/logout/`

**method:** `GET`



### This API provide permission of user

Permission provide a user having which tpye of permission to access the API

**route:** `/api/permission/`

**method:** `POST`

**requestBody:** 

*application/json*

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| permissionname | string | True |  |
| permissionview | string | True |  |
| id | string | False |  |



### This API Show Permission

Permission get show us which tpye of permission user having

**route:** `/api/permission/get/{id}/`

**method:** `GET`

**parameters:** 

| name | type | in   | required | description |
| ---- | ---- | ---- | -------- | ----------- |
| id | string | path | True |  |



### This API assign role of user

User role assign the role of user and what they access in API

**route:** `/api/role/`

**method:** `POST`

**requestBody:** 

*application/json*

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| rolename | string | True |  |
| permissions | array | True |  |
| id | string | False |  |



### This API Show role of user

Role get API provide user role and Accessibility of user

**route:** `/api/role/get/{id}/`

**method:** `GET`

**parameters:** 

| name | type | in   | required | description |
| ---- | ---- | ---- | -------- | ----------- |
| id | string | path | True |  |




## venture

venture

### This API create venture

Venture create API create venture_capital in this name and type are required

**route:** `/api/venture/venture/`

**method:** `POST`

**requestBody:** 

*application/json*

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| name | string | True |  |
| type | string | True |  |
| email | string | True |  |
| user_id | string | True |  |
| Assotiation_id | array | False |  |
| Timestamp | date-time | False |  |
| id | string | False |  |



### This API provide all venture detail

Venture getall provide all the venture and detail about the venture

**route:** `/api/venture/venture/getall/`

**method:** `GET`



### This API provide venture detail

Venture get provide the detail about particular venture detail by providing the ID

**route:** `/api/venture/venture/get/{objectid}/`

**method:** `GET`

**parameters:** 

| name | type | in   | required | description |
| ---- | ---- | ---- | -------- | ----------- |
| id | string | path | True |  |



### This API update venture

Venture update provide update

**route:** `/api/venture/venture/update/{objectid}/`

**method:** `PUT`

**parameters:** 

| name | type | in   | required | description |
| ---- | ---- | ---- | -------- | ----------- |
| id | string | path | True |  |



### This API delete venture

Venture delete takes object ID to delete particular venture

**route:** `/api/venture/venture/delete/{objectid}/`

**method:** `DELETE`

**parameters:** 

| name | type | in   | required | description |
| ---- | ---- | ---- | -------- | ----------- |
| id | string | path | True |  |




## schemas

### Candidate

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| firstname | string | True |  |
| lastname | string | True |  |
| email | string | True |  |
| about | - | - | [About.__pydantic_model__](#About.__pydantic_model__) |
| careerplan | - | - | [CareerPlan.__pydantic_model__](#CareerPlan.__pydantic_model__) |
| finalbits | - | - | [FinalBits.__pydantic_model__](#FinalBits.__pydantic_model__) |
| id | string | False |  |


### About.__pydantic_model__

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| nativeplace | string | True |  |
| functionalexpertise | string | True |  |
| gender | string | True |  |
| ethnicity | string | True |  |
| linkedin | string | True |  |


### CareerPlan.__pydantic_model__

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| work | string | True |  |
| careerlevel | string | True |  |
| capital | string | True |  |
| industry | string | True |  |
| workplace | string | True |  |
| experience | string | True |  |


### FinalBits.__pydantic_model__

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| document | binary | True |  |
| extrainformation | string | True |  |
| termsandconditions | boolean | True |  |


### UnprocessableEntity

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| loc | array | False | the error's location as a list.  |
| msg | string | False | a computer-readable identifier of the error type. |
| type_ | string | False | a human readable explanation of the error. |
| ctx | object | False | an optional object which contains values required to render the error message. |


### Response

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| data |  | False |  |
| status_code | integer | True |  |


### User

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| firstname | string | True |  |
| lastname | string | True |  |
| email | string | True |  |
| password | string | True |  |
| role | string | False |  |
| id | string | False |  |


### UserLogin

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| email | string | True |  |
| password | string | True |  |


### Permission

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| permissionname | string | True |  |
| permissionview | string | True |  |
| id | string | False |  |


### Role

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| rolename | string | True |  |
| permissions | array | True |  |
| id | string | False |  |


### CompanyMaster

| name | type | required | description |
| ---- | ---- | -------- | ----------- |
| name | string | True |  |
| type | string | True |  |
| email | string | True |  |
| user_id | string | True |  |
| Assotiation_id | array | False |  |
| Timestamp | date-time | False |  |
| id | string | False |  |


# testtask
