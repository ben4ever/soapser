Design
======
* Look at ``examples/complex.py``.
* Why does ``_returns=Array(User)`` create 2 elements?
  ::

    <xs:complexType name="list_usersResponse">
      <xs:sequence>
        <xs:element name="list_usersResult0" type="s1:User" minOccurs="0" nillable="true"/>
        <xs:element name="list_usersResult1" type="s1:User" minOccurs="0" nillable="true"/>
      </xs:sequence>
    </xs:complexType>

Testing
=======
* Use ``examples/testing/helloworld_null.py``.

TODO
====
* WSDL should have ``soapAction="Flow/Services/Custom/receiveItemBarCode"``
