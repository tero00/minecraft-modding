package ter0minator.untiered;

import net.minecraft.inventory.EntityEquipmentSlot;
import net.minecraft.item.ItemArmor;

public class Armor extends ItemArmor {

	public Armor(String name, ItemArmor.ArmorMaterial materialIn, int renderIndexIn, EntityEquipmentSlot equipmentSlotIn) {
		super(materialIn, renderIndexIn, equipmentSlotIn);
		setRegistryName(name);
		setUnlocalizedName(name);
		setCreativeTab(Untiered.UNTIERED_TAB);
	}
}

