from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlDuration, XmlTime

from my_package.urn_entsoe_eu_wgedi_codelists import (
    StandardAssetTypeList,
    StandardBusinessTypeList,
    StandardCodingSchemeTypeList,
    StandardCurveTypeList,
    StandardMessageTypeList,
    StandardProcessTypeList,
    StandardReasonCodeTypeList,
    StandardRoleTypeList,
    StandardStatusTypeList,
    StandardUnitOfMeasureTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0"


@dataclass
class EsmpDateTimeInterval:
    class Meta:
        name = "ESMP_DateTimeInterval"

    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        },
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        },
    )


@dataclass
class Point:
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )
    quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
        },
    )


class UnitSymbol(Enum):
    """
    :cvar A: Current in ampere.
    :cvar DEG: Plane angle in degrees.
    :cvar DEG_C: Relative temperature in degrees Celsius. In the SI unit
        system the symbol is ºC. Electric charge is measured in coulomb
        that has the unit symbol C. To destinguish degree Celsius form
        coulomb the symbol used in the UML is degC. Reason for not using
        ºC is the special character º is difficult to manage in
        software.
    :cvar F: Capacitance in farad.
    :cvar G: Mass in gram.
    :cvar H: Time in hours.
    :cvar H_1: Inductance in henry.
    :cvar HZ: Frequency in hertz.
    :cvar J: Energy in joule.
    :cvar KVT: kV as per UN/CEFACT recommendation 20.
    :cvar M: Length in meter.
    :cvar M2: Area in square meters.
    :cvar M3: Volume in cubic meters.
    :cvar MAW: MW as per UN/CEFACT recommendation 20.
    :cvar MIN: Time in minutes.
    :cvar N: Force in newton.
    :cvar NONE: Dimension less quantity, e.g. count, per unit, etc.
    :cvar OHM: Resistance in ohm.
    :cvar PA: Pressure in pascal (n/m2).
    :cvar RAD: Plane angle in radians.
    :cvar S: Time in seconds.
    :cvar S_1: Conductance in siemens.
    :cvar V: Voltage in volt.
    :cvar VA: Apparent power in volt ampere.
    :cvar VAH: Apparent energy in volt ampere hours.
    :cvar VAR: Reactive power in volt ampere reactive.
    :cvar VARH: Reactive energy in volt ampere reactive hours.
    :cvar W: Active power in watt.
    :cvar WH: Real energy in what hours.
    :cvar WTT: W as per UN/CEFACT recommendation 20.
    """

    A = "A"
    DEG = "deg"
    DEG_C = "degC"
    F = "F"
    G = "g"
    H = "h"
    H_1 = "H"
    HZ = "Hz"
    J = "J"
    KVT = "KVT"
    M = "m"
    M2 = "m2"
    M3 = "m3"
    MAW = "MAW"
    MIN = "min"
    N = "N"
    NONE = "none"
    OHM = "ohm"
    PA = "Pa"
    RAD = "rad"
    S = "s"
    S_1 = "S"
    V = "V"
    VA = "VA"
    VAH = "VAh"
    VAR = "VAr"
    VARH = "VArh"
    W = "W"
    WH = "Wh"
    WTT = "WTT"


@dataclass
class ActionStatus:
    class Meta:
        name = "Action_Status"

    value: Optional[Union[StandardStatusTypeList, str]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
        },
    )


@dataclass
class AreaIdString:
    class Meta:
        name = "AreaID_String"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 18,
        },
    )
    coding_scheme: Optional[Union[StandardCodingSchemeTypeList, str]] = field(
        default=None,
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EsmpActivePower:
    class Meta:
        name = "ESMP_ActivePower"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([0-9]*\.?[0-9]*)",
        },
    )
    unit: UnitSymbol = field(
        init=False,
        default=UnitSymbol.MAW,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PartyIdString:
    class Meta:
        name = "PartyID_String"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 16,
        },
    )
    coding_scheme: Optional[Union[StandardCodingSchemeTypeList, str]] = field(
        default=None,
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Reason:
    code: Optional[Union[StandardReasonCodeTypeList, str]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "max_length": 512,
        },
    )


@dataclass
class ResourceIdString:
    class Meta:
        name = "ResourceID_String"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 60,
        },
    )
    coding_scheme: Optional[Union[StandardCodingSchemeTypeList, str]] = field(
        default=None,
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SeriesPeriod:
    class Meta:
        name = "Series_Period"

    time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
        },
    )
    resolution: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
        },
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "min_occurs": 1,
        },
    )


@dataclass
class AssetRegisteredResource:
    class Meta:
        name = "Asset_RegisteredResource"

    m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    asset_psrtype_psr_type: Optional[Union[StandardAssetTypeList, str]] = (
        field(
            default=None,
            metadata={
                "name": "asset_PSRType.psrType",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            },
        )
    )
    location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )


@dataclass
class TimeSeries:
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
            "max_length": 35,
        },
    )
    business_type: Optional[Union[StandardBusinessTypeList, str]] = field(
        default=None,
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
        },
    )
    bidding_zone_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "biddingZone_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    start_date_and_or_time_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "start_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
        },
    )
    start_date_and_or_time_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "start_DateAndOrTime.time",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
        },
    )
    end_date_and_or_time_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "end_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
        },
    )
    end_date_and_or_time_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "end_DateAndOrTime.time",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
        },
    )
    quantity_measure_unit_name: Optional[
        Union[StandardUnitOfMeasureTypeList, str]
    ] = field(
        default=None,
        metadata={
            "name": "quantity_Measure_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
        },
    )
    curve_type: Optional[Union[StandardCurveTypeList, str]] = field(
        default=None,
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
            "required": True,
        },
    )
    production_registered_resource_m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    production_registered_resource_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    production_registered_resource_location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    production_registered_resource_p_srtype_psr_type: Optional[
        Union[StandardAssetTypeList, str]
    ] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.pSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    production_registered_resource_p_srtype_power_system_resources_m_rid: Optional[
        ResourceIdString
    ] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.pSRType.powerSystemResources.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    production_registered_resource_p_srtype_power_system_resources_name: Optional[
        str
    ] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.pSRType.powerSystemResources.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    production_registered_resource_p_srtype_power_system_resources_nominal_p: Optional[
        EsmpActivePower
    ] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.pSRType.powerSystemResources.nominalP",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    asset_registered_resource: list[AssetRegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "Asset_RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    available_period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Available_Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    wind_power_feedin_period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "WindPowerFeedin_Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0",
        },
    )


@dataclass
class UnavailabilityMarketDocument:
    class Meta:
        name = "Unavailability_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:0"

    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "required": True,
            "max_length": 35,
        },
    )
    revision_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "revisionNumber",
            "type": "Element",
            "required": True,
            "pattern": r"[1-9]([0-9]){0,2}",
        },
    )
    type_value: Optional[Union[StandardMessageTypeList, str]] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    process_process_type: Optional[Union[StandardProcessTypeList, str]] = (
        field(
            default=None,
            metadata={
                "name": "process.processType",
                "type": "Element",
                "required": True,
            },
        )
    )
    created_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        },
    )
    sender_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "sender_MarketParticipant.mRID",
            "type": "Element",
            "required": True,
        },
    )
    sender_market_participant_market_role_type: Optional[
        Union[StandardRoleTypeList, str]
    ] = field(
        default=None,
        metadata={
            "name": "sender_MarketParticipant.marketRole.type",
            "type": "Element",
            "required": True,
        },
    )
    receiver_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "receiver_MarketParticipant.mRID",
            "type": "Element",
            "required": True,
        },
    )
    receiver_market_participant_market_role_type: Optional[
        Union[StandardRoleTypeList, str]
    ] = field(
        default=None,
        metadata={
            "name": "receiver_MarketParticipant.marketRole.type",
            "type": "Element",
            "required": True,
        },
    )
    unavailability_time_period_time_interval: Optional[
        EsmpDateTimeInterval
    ] = field(
        default=None,
        metadata={
            "name": "unavailability_Time_Period.timeInterval",
            "type": "Element",
            "required": True,
        },
    )
    doc_status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "name": "docStatus",
            "type": "Element",
        },
    )
    time_series: list[TimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "TimeSeries",
            "type": "Element",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
        },
    )
