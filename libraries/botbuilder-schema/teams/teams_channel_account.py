# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

from botbuilder.schema import ChannelAccount

class TeamsChannelAccount(ChanelAccount):
    def __init__(self, id: string = "", name: string = "", given_name: string = "", surname: string = "", email: string = "", user_principal_name: string = ""):
        self.id = id
        self.name = name
        self.given_name = given_name
        self.surname = surname
        self.email = email
        self.user_principal_name = user_principal_name

    @property
    def given_name():
        return self.given_name

    @property 
    def surname():
        return self.surname

    @property
    def email():
        return self.email

    @property
    def user_principal_name():
        return self.user_principal_name