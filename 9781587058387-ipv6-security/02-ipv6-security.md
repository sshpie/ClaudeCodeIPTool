# IPv6 Security

### Scott Hogg, CCIE No. 5133  
Eric Vyncke

**Cisco Press**

Cisco Press  
800 East 96th Street  
Indianapolis, IN 46240 USA

**IPv6 Security**

Scott Hogg and Eric Vyncke

Copyright© 2009 Cisco Systems, Inc.

Published by:  
 Cisco Press  
 800 East 96th Street  
 Indianapolis, IN 46240 USA

All rights reserved. No part of this book may be reproduced or transmitted in any form or by any means, electronic or mechanical, including photocopying, recording, or by any information storage and retrieval system, without written permission from the publisher, except for the inclusion of brief quotations in a review.

Printed in the United States of America

First Printing December 2008

Library of Congress Cataloging-in-Publication Data:

Hogg, Scott.  
    IPv6 security / Scott Hogg, Eric Vyncke.  
      p. cm.  
    Includes bibliographical references and index.  
    ISBN-13: 978-1-58705-594-2 (pbk.)  
    ISBN-10: 1-58705-594-5  
    1. Computer networks—Security measures. 2. TCP/IP (Computer network protocol) I. Vyncke, Eric. II. Title.  
   
    TK5105.59.H637 2009  
    005.8—dc22  
                                        2008047255

ISBN-13: 978-1-58705-594-2

ISBN-10: 1-58705-594-5

**Warning and Disclaimer**

This book is designed to provide information about the security aspects of the IPv6 protocol. Every effort has been made to make this book as complete and as accurate as possible, but no warranty or fitness is implied.

The information is provided on an “as is” basis. The authors, Cisco Press, and Cisco Systems, Inc., shall have neither liability nor responsibility to any person or entity with respect to any loss or damages arising from the information contained in this book or from the use of the discs or programs that may accompany it.

The opinions expressed in this book belong to the author and are not necessarily those of Cisco Systems, Inc.

**Trademark Acknowledgments**

All terms mentioned in this book that are known to be trademarks or service marks have been appropriately capitalized. Cisco Press or Cisco Systems, Inc., cannot attest to the accuracy of this information. Use of a term in this book should not be regarded as affecting the validity of any trademark or service mark.

**Feedback Information**

At Cisco Press, our goal is to create in-depth technical books of the highest quality and value. Each book is crafted with care and precision, undergoing rigorous development that involves the unique expertise of members from the professional technical community.

Readers’ feedback is a natural continuation of this process. If you have any comments regarding how we could improve the quality of this book, or otherwise alter it to better suit your needs, you can contact us through email at [feedback@ciscopress.com](mailto:feedback@ciscopress.com). Please make sure to include the book title and ISBN in your message.

We greatly appreciate your assistance.

**Corporate and Government Sales**

The publisher offers excellent discounts on this book when ordered in quantity for bulk purchases or special sales, which may include electronic versions and/or custom covers and content particular to your business, training goals, marketing focus, and branding interests. For more information, please contact:

**U.S. Corporate and Government Sales**  
 1-800-382-3419  
 [corpsales@pearsontechgroup.com](mailto:corpsales@pearsontechgroup.com)

For sales outside the United States please contact:

**International Sales**  
 [international@pearsoned.com](mailto:international@pearsoned.com)

|  |  |
| --- | --- |
| Publisher | Paul Boger |
| Associate Publisher | Dave Dusthimer |
| Cisco Press Program Manager | Jeff Brady |
| Executive Editor | Brett Bartow |
| Managing Editor | Patrick Kanouse |
| Development Editor | Dayna Isley |
| Senior Project Editor | Tonya Simpson |
| Copy Editor | Written Elegance, Inc. |
| Technical Editors | Joseph Karpenko, Darrin Miller |
| Editorial Assistant | Vanessa Evans |
| Book and Cover Designer | Louisa Adair |
| Composition | Mark Shirar |
| Indexer | Bill Meyers |
| Proofreader | Leslie Joseph |

![image](/api/v2/epubs/urn:orm:book:9781587058387/files/graphics/cisco.jpg)

**Americas Headquarters**  
 Cisco Systems, Inc.  
 San Jose, CA  
   
 **Asia Pacific Headquarters**  
 Cisco Systems (USA) Pte. Ltd.  
 Singapore  
   
 **Europe Headquarters**  
 Cisco Systems International BV  
 Amsterdam, The Netherlands

Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco Website at **[www.cisco.com/go/offices](http://www.cisco.com/go/offices)**.

CCDE, CCENT, Cisco Eos, Cisco Lumin, Cisco Nexus, Cisco StadiumVision, the Cisco logo, DCE, and Welcome to the Human Network are trademarks.; Changing the Way We Work, Live, Play, and Learn is a service mark; and Access Registrar, Aironet, AsyncOS, Bringing the Meeting To You, Catalyst, CCDA, CCDP, CCIE, CCIP, CCNA, CCNP, CCSP, CCVP, Cisco, the Cisco Certified Internetwork Expert logo, Cisco IOS, Cisco Press, Cisco Systems, Cisco Systems Capital, the Cisco Systems logo, Cisco Unity, Collaboration Without Limitation, EtherFast, EtherSwitch, Event Center, Fast Step, Follow Me Browsing, FormShare, GigaDrive, HomeLink, Internet Quotient, IOS, iPhone, iQ Expertise, the iQ logo, iQ Net Readiness Scorecard, iQuick Study, IronPort, the IronPort logo, LightStream, Linksys, MediaTone, MeetingPlace, MGX, Networkers, Networking Academy, Network Registrar, PCNow, PIX, PowerPanels, ProConnect, ScriptShare, SenderBase, SMARTnet, Spectrum Expert, StackWise, The Fastest Way to Increase Your Internet Quotient, TransPath, WebEx, and the WebEx logo are registered trademarks of Cisco Systems, Inc. and/or its affiliates in the United States and certain other countries.

All other trademarks mentioned in this document or Website are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (0805R)

## Dedications

This book is dedicated to David Hogg. I think he would be proud of me.

—Scott Hogg

To my family, my parents Ghislaine and Willy, my wife Isabelle, and my children Pierre and Thibault.

—Eric Vyncke
