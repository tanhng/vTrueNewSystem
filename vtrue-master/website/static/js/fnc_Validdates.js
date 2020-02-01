function	ValidDateTo(oLicenseFrom,oLicenseTo)
{
	var dtFromDate, dtToDate;
	dtFromDate	=	new Date(eval(oLicenseFrom).value);
	dtToDate	=	new Date(eval(oLicenseTo).value);
	if (dtFromDate>dtToDate)
	{
		alert("End Date must be greater than Start Date!");
		eval(oLicenseTo).focus();
		return false;
	}
}
//==============================================================================

function isDate( s )
	{
		var sDay, sMonth, sYear, nMonth, nDay, nYear, nSep1, nSep2;
		nSep1 = s.indexOf( "/" );	if ( nSep1 < 0 ) return false;
		nSep2 = s.lastIndexOf( "/" );	if ( nSep2 < 0 ) return false;
		if ( nSep1 == nSep2 ) return false;

		sDay = s.substring( 0, nSep1  );
		sMonth = s.substring( nSep1 + 1, nSep2 );
		sYear = s.substring( nSep2+1 );
		if ( !sMonth.length || !sDay.length || sYear.length <4) return false;
		// isNaN(empty) is false
		if ( isNaN(sMonth) || isNaN(sDay) || isNaN(sYear) ) return false;
		nMonth = parseInt(sMonth,10); nDay = parseInt(sDay,10); nYear = parseInt(sYear,10);
		if ( nMonth<=0 || nDay<=0 || nYear<0 ) return false;
		if ( nMonth > 12 ) return false;
		if (nMonth==1 || nMonth==3 || nMonth==5 || nMonth==7 || nMonth==8 || nMonth==10 || nMonth==12 )
			if ( nDay > 31 ) return false; 
		if (nMonth==4 || nMonth==6 || nMonth==9 || nMonth==11 )
			if ( nDay > 30 ) return false; 
		if (nMonth==2) {
			if ( (nYear % 4 == 0) && (nYear % 100 != 0)) { // leap year
				if ( nDay > 29 ) return false;
			} else if ( nDay > 28 ) return false;
		}
		return true;
	} // isDate function
//======================================	

function	ValidDates(oParentForm, arrObjName, blnAlert)
{
	//===============================================
	function	JTrimDate(s)
	{
		var i, sRetVal = "";
		i = s.length-1;
		while ( i>=0 && s.charAt(i) == ' ' ) i--;
		s = s.substring( 0, i+1 ); // trim blanks on the right
		i = 0;
		while ( i< s.length && s.charAt(i) == ' ') i++;
		return s.substring( i );
	}
	//===============================================
	function	GetCurrentDate()
	{
		var dt,month,day,year, st;
		dt	= new Date();
		month	= dt.getMonth()+1;
		day	= dt.getDate();
		year	= dt.getFullYear();
		st	= day + '/' + month + '/' + year;
		return	st;
	}
	//===============================================
	function isDate( s )
	{
		var sDay, sMonth, sYear, nMonth, nDay, nYear, nSep1, nSep2;
		nSep1 = s.indexOf( "/" );	if ( nSep1 < 0 ) return false;
		nSep2 = s.lastIndexOf( "/" );	if ( nSep2 < 0 ) return false;
		if ( nSep1 == nSep2 ) return false;

		sMonth = s.substring( 0, nSep1  );
		sDay = s.substring( nSep1 + 1, nSep2 );
		sYear = s.substring( nSep2+1 );
		if ( !sMonth.length || !sDay.length || sYear.length <4) return false;
		// isNaN(empty) is false
		if ( isNaN(sMonth) || isNaN(sDay) || isNaN(sYear) ) return false;
		nMonth = parseInt(sMonth,10); nDay = parseInt(sDay,10); nYear = parseInt(sYear,10);
		if ( nMonth<=0 || nDay<=0 || nYear<0 ) return false;
		if ( nMonth > 12 ) return false;
		if (nMonth==1 || nMonth==3 || nMonth==5 || nMonth==7 || nMonth==8 || nMonth==10 || nMonth==12 )
			if ( nDay > 31 ) return false; 
		if (nMonth==4 || nMonth==6 || nMonth==9 || nMonth==11 )
			if ( nDay > 30 ) return false; 
		if (nMonth==2) {
			if ( (nYear % 4 == 0) && (nYear % 100 != 0)) { // leap year
				if ( nDay > 29 ) return false;
			} else if ( nDay > 28 ) return false;
		}
		return true;
	} // isDate function
	//===============================================
	frmParent	=	oParentForm;
	intLength	=	arrObjName.length;
	var	i,stDate;
	for (i=0;i<intLength;i++)
	{
		if (frmParent(arrObjName[i])!=null)	
		{
			stDate	=	JTrimDate(frmParent(arrObjName[i]).value);
			if (stDate.length==0) break;
			if ((stDate=="")||(!isDate(stDate)))
			{
				if (blnAlert)
				{
					stName	=	frmParent(arrObjName[i]).name;
					stName	=	stName.replace(/txt/i,"");
					stName	=	stName.replace(/cbo/i,"");
					if (typeof(SeparateName)=='function')
						stName	=	SeparateName(stName);
					alert("Invalid "+ stName+"!");
					frmParent(arrObjName[i]).focus();
				}
			}
			else
			{
				var	dt,year;
				dt = new Date(stDate);
				year = dt.getFullYear();
			
				if ((parseInt(year)<1753)||(parseInt(year)>9999))
				{
					if (blnAlert) alert("Year must be between 1753 and 9999");
					frmParent(arrObjName[i]).focus();
					return false;
				}
			}
		}
		else
		{
			if (!confirm("\""+arrObjName[i]+"\" is not a control of form "+frmParent.name+"!\nDo you want to continue?"))
				return	false;
		}
	}
	return	true;
}
