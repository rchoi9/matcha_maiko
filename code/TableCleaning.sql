/*
 * May Later address: 
 * 1. Fields in common: 'Gross Sales', 'Discounts', 'Net Sales',
 * 						'Event Type', 'Customer ID', 'Customer Name'
 * 2. Create a Customers table and separate the data in the backend
 * 
 * Notes about Fields:
 * Gross Sale: Total $ value of sale before discounts excluding tax
 * Net Sale: $ value of sale including discounts
 * Total Collected: Total $ collected including tax and tip
 * Net Total: Total $ that goes to the business, after credit card processing fees are deducted
 * 
 * In an ideal world:
 * Best Practice would be to separate fields and create columns 'Customer' and 'Payment'* 
 * 'Customer' ISSUE Null Values: Customer ID, Customer Name 
 * 'Payment' Should contain payment details: Payment ID, PAN Suffix, Card, Square Gift Card
 * 'Transactions' Should contain transaction details: fees, tax, tips, source, Card Entry Methods, Event Type
 * However, there are missing values in Customer ID, Payment ID, and Transaction ID 
 * because those values are not generated for cash transactions. 
 */
select transactions."Customer Name" 
from transactions  
where transactions."Customer ID" is "M1ZF71KRJD1TB41TSEXST8TJGR"


select *
from items

select items."Transaction ID", items."Price Point Name" 
from items
where "Price Point Name" is not NULL

select
	t."Transaction ID",
	t."Payment ID",
	t."Source",
	t."Event Type",
	t.Date,
	t.Time,
	t."Gross Sales",
	t."Net Sales",
	t."Net Total",
	t."Total Collected",
	t."Discount Name",
	t.Discounts,
	t.Tip,
	t."Service Charges",
	t.Tax,
	t.Fees,
	t."Fee Percentage Rate",
	t."Fee Fixed Rate",
	t."Partial Refunds",
	t.Cash,
	t.Card,
	t."Card Brand",
	t."PAN Suffix",
	t."Card Entry Methods",
	t."Gift Card Sales",
	t."Square Gift Card",
	t."Customer ID",
	t."Customer Name",
	i.Category,
	i.Item,
	i.Qty,
	i."Price Point Name",
	i."Modifiers Applied" 
from
	transactions t
inner join items i on
	t."Transaction ID" = i."Transaction ID" 

-- Modifying Data Types
-- ALTER TABLE items RENAME COLUMN Date TO DateTmp;

alter transactions
modify column "Pan Suffix" VARCHAR(50);

# Items 
# Deleting Unecessary Columns

-- EST
alter table items
	drop "Time Zone";
	
-- Not Applicable
alter table items	
	drop SKU;

-- Use to join data
/*alter table transactions 
	drop "Transaction ID";*/

-- Will be in Transaction Dataset
alter table items 
	drop "Payment ID";

-- Not Applicable
alter table items
	drop "Device Name";

-- Description of Menu Item
alter table items
	drop  "Notes";

-- Link to Transaction detail
alter table items
	drop  "Details";

-- Not Applicable
alter table items
	drop "Location";
	
-- Not Applicable
alter table items
	drop "Dining Option";
	
-- Not Applicable
alter table items
	drop "Customer Reference ID";

-- Not Applicable
alter table items
	drop "Unit";

-- Same as Qty
alter table items
	drop "Count";

-- Not Applicable
alter table items
	drop "Itemization Type";

-- Not Applicable
alter table items
	drop "Commission";

-- Not Accurate and not going to be used in this project
alter table items
	drop "Employee";

-- Will be in Transaction Dataset
alter table items
	drop "Event Type";

-- Will be in Transaction Dataset
alter table items
	drop "Gross Sales";

-- Will be in Transaction Dataset
alter table items
	drop "Discounts";

-- Will be in Transaction Dataset
alter table items
	drop "Net Sales";

-- Will be in Transaction Dataset
alter table items
	drop "Tax";

-- Will be in Transaction Dataset
alter table items
	drop "Customer ID";

-- Will be in Transaction Dataset
alter table items
	drop "Customer Name";

# Transactions
# Deleting Uncessessary Columns

-- EST
alter table transactions 
	drop "Time Zone";

-- Not Applicable
alter table transactions 
	drop "Other Tender";

-- Not Applicable
alter table transactions 
	drop "Other Tender Type";

-- Not Applicable
alter table transactions 
	drop "Other Tender Note";
	
-- Use to join data
/*alter table transactions 
	drop "Transaction ID";*/

/*alter table transactions 
	drop "Payment ID";*/

-- Not Applicable
alter table transactions 
	drop "Device Name";

-- Not Applicable
alter table transactions 
	drop "Staff Name";

-- Not Applicable
alter table transactions 
	drop "Staff ID";

-- Not Applicable, URL with transaction detail
alter table transactions 
	drop "Details";

-- Description of purchase, included in items
alter table transactions 
	drop "Description";

-- Not Applicable
alter table transactions 
	drop "Location";

-- Not Applicable
alter table transactions 
	drop "Dining Option";

-- Not Applicable
alter table transactions 
	drop "Customer Reference ID";

-- Not Applicable
alter table transactions 
	drop "Device Nickname";

-- Not Applicable
alter table transactions 
	drop "Deposit ID";

-- Not Applicable
alter table transactions 
	drop "Deposit Date";

-- Not Applicable, URL with deposit details
alter table transactions 
	drop "Deposit Details";

-- Not Accurate Data
alter table transactions 
	drop "Refund Reason";

-- Not Applicable
alter table transactions 
	drop "Transaction Status";

-- Not Applicable
alter table transactions 
	drop "Order Reference ID";
	
